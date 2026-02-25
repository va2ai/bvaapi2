#!/usr/bin/env python3
"""Chunking logic for CFR Part 3, Part 4, and KnowVA content."""

import hashlib
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Chunk:
    id: str
    text: str
    metadata: Dict[str, str]
    source_url: Optional[str] = None


def _make_id(*parts: str) -> str:
    """Deterministic chunk ID for idempotent upsert."""
    raw = ":".join(str(p) for p in parts)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def chunk_cfr_part4(
    section_markdown: str,
    part: str,
    section: str,
    dc_lookup: Dict[str, Dict[str, str]],
) -> List[Chunk]:
    """Chunk a Part 4 rating criteria section by diagnostic code boundaries."""
    if not section_markdown or not section_markdown.strip():
        return []

    # Find DCs that map to this section
    section_dcs = {
        dc: info for dc, info in dc_lookup.items()
        if info["part"] == part and info["section"] == section
    }

    # Try to split on DC code patterns (4-digit codes like 9411, 6847)
    dc_pattern = re.compile(r"(?:^|\n)(\d{4})\s", re.MULTILINE)
    splits = list(dc_pattern.finditer(section_markdown))

    chunks = []
    if len(splits) >= 2:
        # Split at each DC boundary
        for i, match in enumerate(splits):
            start = match.start()
            end = splits[i + 1].start() if i + 1 < len(splits) else len(section_markdown)
            dc_code = match.group(1)
            text = section_markdown[start:end].strip()
            if len(text) < 20:
                continue
            dc_info = section_dcs.get(dc_code, {})
            meta = {
                "source": "cfr",
                "part": part,
                "section": section,
                "content_type": "rating_criteria",
            }
            if dc_code in dc_lookup:
                meta["dc"] = dc_code
                meta["condition"] = dc_lookup[dc_code].get("condition", "")
                meta["schedule"] = dc_lookup[dc_code].get("schedule", "")
            chunks.append(Chunk(
                id=_make_id("cfr", part, section, dc_code),
                text=text[:3000],
                metadata=meta,
                source_url=f"https://www.ecfr.gov/current/title-38/part-{part}/section-{part}.{section}",
            ))
    else:
        # Keep whole section as one chunk
        schedule = ""
        for info in section_dcs.values():
            schedule = info.get("schedule", "")
            break
        meta = {
            "source": "cfr",
            "part": part,
            "section": section,
            "content_type": "rating_criteria",
        }
        if schedule:
            meta["schedule"] = schedule
        chunks.append(Chunk(
            id=_make_id("cfr", part, section, "full"),
            text=section_markdown[:4000].strip(),
            metadata=meta,
            source_url=f"https://www.ecfr.gov/current/title-38/part-{part}/section-{part}.{section}",
        ))

    return chunks


def chunk_cfr_part3(
    section_markdown: str,
    part: str,
    section: str,
) -> List[Chunk]:
    """Chunk a Part 3 adjudication section at subsection boundaries."""
    if not section_markdown or not section_markdown.strip():
        return []

    # Split on subsection markers like (a), (b), (c)
    subsection_pattern = re.compile(r"\n\([a-z]\)\s")
    splits = list(subsection_pattern.finditer(section_markdown))

    # Extract header (everything before first subsection)
    header = ""
    if splits:
        header = section_markdown[:splits[0].start()].strip()
        if len(header) > 500:
            header = header[:500]

    chunks = []
    if len(splits) >= 2:
        for i, match in enumerate(splits):
            start = match.start()
            end = splits[i + 1].start() if i + 1 < len(splits) else len(section_markdown)
            text = section_markdown[start:end].strip()
            # Merge short subsections with context
            if len(text) < 100 and i + 1 < len(splits):
                continue
            # Prepend section header for context
            full_text = f"38 CFR {part}.{section}\n{header}\n\n{text}" if header else text
            subsection_letter = re.search(r"\(([a-z])\)", text)
            sub_id = subsection_letter.group(1) if subsection_letter else str(i)
            chunks.append(Chunk(
                id=_make_id("cfr", part, section, sub_id),
                text=full_text[:3000],
                metadata={
                    "source": "cfr",
                    "part": part,
                    "section": section,
                    "content_type": "adjudication",
                },
                source_url=f"https://www.ecfr.gov/current/title-38/part-{part}/section-{part}.{section}",
            ))
    else:
        # No subsection splits found - keep whole section
        chunks.append(Chunk(
            id=_make_id("cfr", part, section, "full"),
            text=section_markdown[:4000].strip(),
            metadata={
                "source": "cfr",
                "part": part,
                "section": section,
                "content_type": "adjudication",
            },
            source_url=f"https://www.ecfr.gov/current/title-38/part-{part}/section-{part}.{section}",
        ))

    return chunks


def chunk_knowva(
    article_markdown: str,
    article_id: int,
    article_name: str,
) -> List[Chunk]:
    """Chunk a KnowVA article by markdown heading boundaries."""
    if not article_markdown or not article_markdown.strip():
        return []

    # Split on markdown headings (## or ###)
    heading_pattern = re.compile(r"(?:^|\n)(#{2,3}\s+.+)")
    splits = list(heading_pattern.finditer(article_markdown))

    chunks = []
    title_prefix = f"# {article_name}\n\n"

    if len(splits) >= 2:
        # Add intro section (before first heading)
        intro_end = splits[0].start()
        intro = article_markdown[:intro_end].strip()
        if len(intro) > 50:
            chunks.append(Chunk(
                id=_make_id("knowva", str(article_id), "intro"),
                text=(title_prefix + intro)[:3000],
                metadata={
                    "source": "knowva",
                    "article_id": str(article_id),
                    "article_name": article_name,
                    "content_type": "guidance",
                },
            ))

        for i, match in enumerate(splits):
            start = match.start()
            end = splits[i + 1].start() if i + 1 < len(splits) else len(article_markdown)
            text = article_markdown[start:end].strip()
            if len(text) < 50:
                continue
            # Prepend article title for context
            full_text = title_prefix + text
            # Split further if too long (~800 tokens ~ 3200 chars)
            if len(full_text) > 3200:
                # Split on paragraph boundaries
                paragraphs = full_text.split("\n\n")
                current = ""
                sub_idx = 0
                for para in paragraphs:
                    if len(current) + len(para) > 3000 and current:
                        chunks.append(Chunk(
                            id=_make_id("knowva", str(article_id), str(i), str(sub_idx)),
                            text=current.strip(),
                            metadata={
                                "source": "knowva",
                                "article_id": str(article_id),
                                "article_name": article_name,
                                "content_type": "guidance",
                            },
                        ))
                        current = title_prefix + para + "\n\n"
                        sub_idx += 1
                    else:
                        current += para + "\n\n"
                if current.strip() and len(current.strip()) > len(title_prefix):
                    chunks.append(Chunk(
                        id=_make_id("knowva", str(article_id), str(i), str(sub_idx)),
                        text=current.strip()[:3000],
                        metadata={
                            "source": "knowva",
                            "article_id": str(article_id),
                            "article_name": article_name,
                            "content_type": "guidance",
                        },
                    ))
            else:
                chunks.append(Chunk(
                    id=_make_id("knowva", str(article_id), str(i)),
                    text=full_text[:3000],
                    metadata={
                        "source": "knowva",
                        "article_id": str(article_id),
                        "article_name": article_name,
                        "content_type": "guidance",
                    },
                ))
    else:
        # No headings - keep whole article as one chunk (or split by paragraphs if long)
        full_text = title_prefix + article_markdown
        if len(full_text) <= 3200:
            chunks.append(Chunk(
                id=_make_id("knowva", str(article_id), "full"),
                text=full_text[:3000],
                metadata={
                    "source": "knowva",
                    "article_id": str(article_id),
                    "article_name": article_name,
                    "content_type": "guidance",
                },
            ))
        else:
            paragraphs = full_text.split("\n\n")
            current = ""
            idx = 0
            for para in paragraphs:
                if len(current) + len(para) > 3000 and current:
                    chunks.append(Chunk(
                        id=_make_id("knowva", str(article_id), str(idx)),
                        text=current.strip()[:3000],
                        metadata={
                            "source": "knowva",
                            "article_id": str(article_id),
                            "article_name": article_name,
                            "content_type": "guidance",
                        },
                    ))
                    current = title_prefix + para + "\n\n"
                    idx += 1
                else:
                    current += para + "\n\n"
            if current.strip() and len(current.strip()) > len(title_prefix):
                chunks.append(Chunk(
                    id=_make_id("knowva", str(article_id), str(idx)),
                    text=current.strip()[:3000],
                    metadata={
                        "source": "knowva",
                        "article_id": str(article_id),
                        "article_name": article_name,
                        "content_type": "guidance",
                    },
                ))

    return chunks
