"""CAVC eFiling client — United States Court of Appeals for Veterans Claims.

Supports:
- Case search by number or party name
- Case summary (parties, counsel, case info)
- Full docket report with all entries
- Document fetch (returns raw PDF bytes or text)

No authentication required for public records.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Any

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

CAVC_BASE = "https://efiling.uscourts.cavc.gov/cmecf/servlet/TransportRoom"
CAVC_DOCS = "https://efiling.uscourts.cavc.gov/docs1"
TIMEOUT = 30.0
MAX_RETRIES = 3


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class DocketEntry:
    date: str
    text: str
    dls_id: str | None = None        # document link ID for PDF fetch
    case_id: str | None = None       # internal case ID
    doc_url: str | None = None       # direct docs1 URL if available


@dataclass
class CaseParty:
    name: str
    role: str                         # "appellant" | "appellee"
    attorneys: list[str] = field(default_factory=list)


@dataclass
class CaseSummary:
    case_number: str
    title: str
    docketed: str
    appeal_from: str
    fee_status: str
    case_type: str
    parties: list[CaseParty] = field(default_factory=list)
    docket_entries: list[DocketEntry] = field(default_factory=list)
    internal_case_id: str | None = None


@dataclass
class CaseSearchResult:
    case_number: str
    title: str
    opening_date: str
    last_docket_entry: str
    origin: str


# ---------------------------------------------------------------------------
# Session factory
# ---------------------------------------------------------------------------

def _make_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=MAX_RETRIES,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    s.headers.update({
        "User-Agent": "VetResearcher/1.0 (legal research tool)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    })
    return s


# ---------------------------------------------------------------------------
# HTML parsing helpers
# ---------------------------------------------------------------------------

def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _parse_search_results(html: str) -> list[CaseSearchResult]:
    soup = BeautifulSoup(html, "html.parser")
    results = []
    # Case selection table rows: each data row has a case number link
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 4:
            # cells[0] concatenates case number (link) + title (inline text)
            # e.g. "24-4591Karissa Wiggins v. Douglas A. Collins"
            cell0 = cells[0].get_text(strip=True)
            m = re.match(r"(\d{2}-\d+)(.*)", cell0)
            if not m:
                continue
            case_num_cell = m.group(1)
            title_cell = m.group(2).strip()
            opening = cells[1].get_text(strip=True) if len(cells) > 1 else ""
            last_entry = cells[3].get_text(strip=True) if len(cells) > 3 else ""
            origin = cells[5].get_text(strip=True) if len(cells) > 5 else ""
            results.append(CaseSearchResult(
                case_number=case_num_cell,
                title=title_cell,
                opening_date=opening,
                last_docket_entry=last_entry,
                origin=origin,
            ))
    return results


def _parse_docket_entries(soup: BeautifulSoup, internal_case_id: str | None) -> list[DocketEntry]:
    entries: list[DocketEntry] = []
    date_pat = re.compile(r"^\d{2}/\d{2}/\d{4}$")

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if not cells:
            continue
        # Date is typically first cell; entry text in the last/main text cell
        date_text = _clean(cells[0].get_text())
        if not date_pat.match(date_text):
            continue

        # Gather all text content for this row
        entry_text = _clean(row.get_text())
        # Strip the leading date
        entry_text = entry_text[len(date_text):].strip()

        # Find any document link (doDocPostURL call)
        dls_id = None
        doc_url = None
        for a in row.find_all("a", onclick=True):
            m = re.search(r"doDocPostURL\('([^']+)'", a["onclick"])
            if m:
                dls_id = m.group(1)
                doc_url = f"{CAVC_DOCS}/{dls_id}"
                break

        entries.append(DocketEntry(
            date=date_text,
            text=entry_text,
            dls_id=dls_id,
            case_id=internal_case_id,
            doc_url=doc_url,
        ))

    return entries


def _parse_parties(soup: BeautifulSoup) -> list[CaseParty]:
    """Extract parties by scanning line-by-line: party name appears on the line
    immediately before its role label ('Appellant' / 'Appellee')."""
    lines = [l.strip() for l in soup.get_text("\n", strip=True).splitlines() if l.strip()]
    parties: list[CaseParty] = []
    seen: set[str] = set()

    for i, line in enumerate(lines):
        role = None
        if line == "Appellant":
            role = "appellant"
        elif line == "Appellee":
            role = "appellee"
        elif line == "Petitioner":
            role = "petitioner"
        elif line == "Respondent":
            role = "respondent"

        if role and i > 0:
            name = lines[i - 1]
            # Skip if it looks like a date, a 'v.' separator, or already captured
            if re.match(r"\d{2}/\d{2}/\d{4}", name) or name in ("v.", ""):
                continue
            # Normalize: strip trailing comma/punctuation for dedup key
            name_key = name.rstrip(",. ")
            if name_key in seen:
                continue
            seen.add(name_key)
            name = name_key

            # Collect attorney lines that follow (up to 8 lines, stop at next party or date)
            attorneys: list[str] = []
            for j in range(i + 1, min(i + 15, len(lines))):
                l = lines[j]
                if l in ("Appellant", "Appellee", "v.") or re.match(r"\d{2}/\d{2}/\d{4}", l):
                    break
                if "Esq." in l or ("Attorney" in l and "Appearance" not in l):
                    atty = l.split(",")[0].strip()
                    if atty and atty not in attorneys:
                        attorneys.append(atty)

            parties.append(CaseParty(name=name, role=role, attorneys=attorneys))

    return parties


def _extract_case_meta(soup: BeautifulSoup, case_number: str) -> dict[str, str]:
    text = soup.get_text(" ", strip=True)
    lines = [l.strip() for l in soup.get_text("\n", strip=True).splitlines() if l.strip()]
    meta: dict[str, str] = {}

    m = re.search(r"Docketed:\s*(\d{2}/\d{2}/\d{4})", text)
    meta["docketed"] = m.group(1) if m else ""

    m = re.search(r"Appeal From:\s*(.+?)(?:Fee Status|Case Type)", text)
    meta["appeal_from"] = _clean(m.group(1)) if m else ""

    m = re.search(r"Fee Status:\s*(.+?)(?:Case Type|$)", text)
    meta["fee_status"] = _clean(m.group(1)) if m else ""

    m = re.search(r"Case Type Information:\s*1\)\s*(.+?)(?:\s+2\)|$)", text)
    meta["case_type"] = _clean(m.group(1)) if m else ""

    # Extract internal case ID from any doDocPostURL call
    m = re.search(r"doDocPostURL\('[^']+','(\d+)'\)", str(soup))
    meta["internal_case_id"] = m.group(1) if m else ""

    # Title: scan lines for "X v. Y" pattern near the case number
    # It appears as "CASE_NUMBER\nTitle" OR after "Case Number:CASE_NUMBER"
    title = case_number
    case_num_pat = re.compile(r"v\.", re.IGNORECASE)
    for i, line in enumerate(lines):
        # Line containing "v." that looks like a case title
        if " v. " in line and len(line) > 10:
            # Prefer the one closest after the case number header
            if case_number in line:
                # e.g. "Case Number:23-5171 Foo v. Bar" — strip leading cruft
                title = re.sub(rf".*{re.escape(case_number)}\s*", "", line).strip() or line
            else:
                title = line
            break
    meta["title"] = _clean(title)

    return meta


# ---------------------------------------------------------------------------
# Main client
# ---------------------------------------------------------------------------

class CavcClient:
    """Client for CAVC public eFiling portal."""

    def __init__(self) -> None:
        self._session = _make_session()

    def _post_form(self, data: dict[str, str]) -> str | None:
        try:
            r = self._session.post(CAVC_BASE, data=data, timeout=TIMEOUT)
            r.raise_for_status()
            return r.text
        except Exception as e:
            logger.warning("CAVC POST error: %s", e)
            return None

    def _get(self, params: dict[str, str]) -> str | None:
        try:
            r = self._session.get(CAVC_BASE, params=params, timeout=TIMEOUT)
            r.raise_for_status()
            return r.text
        except Exception as e:
            logger.warning("CAVC GET error: %s", e)
            return None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search_cases(
        self,
        case_number: str = "",
        party_name: str = "",
        open_closed: str = "both",
    ) -> list[CaseSearchResult]:
        """Search for cases by number or party name."""
        html = self._post_form({
            "servlet": "CaseSelectionTable.jsp",
            "csnum1": case_number,
            "csnum2": "",
            "aName": party_name,
            "searchPty": "pty",
            "open_closed": open_closed,
            "sortby": "casenumber",
            "sortbyorder": "asc",
        })
        if not html:
            return []
        return _parse_search_results(html)

    def get_case_summary(self, case_number: str) -> CaseSummary | None:
        """Fetch case summary with parties and counsel."""
        html = self._get({
            "servlet": "CaseSummary.jsp",
            "caseNum": case_number,
            "incOrigDkt": "Y",
            "incDktEntries": "Y",
        })
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")
        meta = _extract_case_meta(soup, case_number)
        parties = _parse_parties(soup)
        entries = _parse_docket_entries(soup, meta.get("internal_case_id"))

        return CaseSummary(
            case_number=case_number,
            title=meta.get("title", case_number),
            docketed=meta.get("docketed", ""),
            appeal_from=meta.get("appeal_from", ""),
            fee_status=meta.get("fee_status", ""),
            case_type=meta.get("case_type", ""),
            parties=parties,
            docket_entries=entries,
            internal_case_id=meta.get("internal_case_id") or None,
        )

    def get_full_docket(self, case_number: str) -> CaseSummary | None:
        """Fetch the full docket report (all entries + document links)."""
        html = self._post_form({
            "servlet": "CaseSummary.jsp",
            "caseNum": case_number,
            "fullDocketReport": "Y",
            "incPrior": "Y",
            "incAssoc": "Y",
            "incPtyAty": "Y",
            "incCaption": "long",
            "incDktEntries": "Y",
            "actionType": "Run Docket Report",
        })
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")
        meta = _extract_case_meta(soup, case_number)
        parties = _parse_parties(soup)
        entries = _parse_docket_entries(soup, meta.get("internal_case_id"))

        return CaseSummary(
            case_number=case_number,
            title=meta.get("title", case_number),
            docketed=meta.get("docketed", ""),
            appeal_from=meta.get("appeal_from", ""),
            fee_status=meta.get("fee_status", ""),
            case_type=meta.get("case_type", ""),
            parties=parties,
            docket_entries=entries,
            internal_case_id=meta.get("internal_case_id") or None,
        )

    def get_document(
        self,
        dls_id: str,
        case_id: str,
        as_text: bool = False,
    ) -> bytes | str | None:
        """Fetch a docket document PDF.

        Args:
            dls_id: Document link ID from docket entry (e.g. '01204214937').
            case_id: Internal case ID from docket page (e.g. '92883').
            as_text: If True, attempt to extract text via pdfplumber (requires install).

        Returns:
            Raw PDF bytes, extracted text string, or None if inaccessible.
        """
        try:
            r = self._session.get(
                CAVC_BASE,
                params={
                    "servlet": "ShowDoc",
                    "dls_id": dls_id,
                    "caseId": case_id,
                    "dktType": "dktPublic",
                },
                timeout=TIMEOUT,
            )
            r.raise_for_status()

            if "text/html" in r.headers.get("Content-Type", ""):
                # Restricted or login-required — returned an HTML error page
                soup = BeautifulSoup(r.text, "html.parser")
                msg = _clean(soup.get_text())
                logger.warning("CAVC doc %s: got HTML (restricted?): %s", dls_id, msg[:200])
                return None

            pdf_bytes = r.content

            if not as_text:
                return pdf_bytes

            # Optional text extraction via pdfplumber
            try:
                import io
                import pdfplumber
                with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
                    return "\n\n".join(
                        page.extract_text() or "" for page in pdf.pages
                    ).strip()
            except ImportError:
                logger.warning("pdfplumber not installed; returning raw bytes")
                return pdf_bytes
            except Exception as e:
                logger.warning("PDF text extraction failed for %s: %s", dls_id, e)
                return pdf_bytes

        except Exception as e:
            logger.warning("CAVC get_document error dls_id=%s: %s", dls_id, e)
            return None

    def get_document_by_entry(
        self,
        entry: DocketEntry,
        as_text: bool = False,
    ) -> bytes | str | None:
        """Convenience wrapper — fetch document for a DocketEntry."""
        if not entry.dls_id or not entry.case_id:
            return None
        return self.get_document(entry.dls_id, entry.case_id, as_text=as_text)

    def find_entry(
        self,
        case_number: str,
        keyword: str,
    ) -> DocketEntry | None:
        """Search full docket for an entry matching a keyword, return first match."""
        summary = self.get_full_docket(case_number)
        if not summary:
            return None
        kw = keyword.lower()
        for entry in summary.docket_entries:
            if kw in entry.text.lower():
                return entry
        return None
