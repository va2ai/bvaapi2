# Federal Register API v1 Documentation

**Source:** https://www.federalregister.gov/developers/documentation/api/v1
**Interactive Docs:** https://www.federalregister.gov/developers/documentation/api/v1
**REST API Overview:** https://www.federalregister.gov/reader-aids/developer-resources/rest-api
**Fetched:** 2026-02-25

---

## Overview

The FederalRegister.gov API provides public access to all Federal Register documents from 1994 to the present. It is a free, open REST API that returns data in JSON or CSV format.

- **No API keys required** - all endpoints are publicly accessible
- **No authentication** - just an HTTP client or browser
- **Data format:** JSON (default) or CSV
- **Pagination limit:** Maximum 2000 results per query (use date filters to retrieve more)
- **Base URL:** `https://www.federalregister.gov/api/v1`

The API covers Federal Register documents (rules, proposed rules, notices, presidential documents), agencies, and public inspection documents. The data is sourced from GPO XML bulk files, normalized and enriched with metadata from OMB, Regulations.gov, and other federal sources.

---

## Authentication

None required. All endpoints are open to the public.

---

## Endpoints

### 1. Search Documents

Search the full corpus of published Federal Register documents.

- **URL:** `GET /api/v1/documents.json`
- **Description:** Search/filter Federal Register documents with full text and metadata filtering.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conditions[term]` | string | No | Full-text search term |
| `conditions[agencies][]` | string (array) | No | Filter by agency slug (e.g., `veterans-affairs-department`). Repeatable. |
| `conditions[type][]` | string (array) | No | Document type: `RULE`, `PRORULE`, `NOTICE`, `PRESDOCU`. Repeatable. |
| `conditions[publication_date][is]` | string (YYYY-MM-DD) | No | Exact publication date |
| `conditions[publication_date][year]` | string (YYYY) | No | Publication year |
| `conditions[publication_date][gte]` | string (YYYY-MM-DD) | No | Published on or after date |
| `conditions[publication_date][lte]` | string (YYYY-MM-DD) | No | Published on or before date |
| `conditions[effective_date][gte]` | string (YYYY-MM-DD) | No | Effective date on or after |
| `conditions[effective_date][lte]` | string (YYYY-MM-DD) | No | Effective date on or before |
| `conditions[docket_id]` | string | No | Filter by docket ID |
| `conditions[regulation_id_number]` | string | No | Filter by RIN (Regulation Identifier Number) |
| `conditions[cfr][title]` | integer | No | CFR title number (e.g., `38` for veterans) |
| `conditions[cfr][part]` | integer | No | CFR part number |
| `conditions[section_ids][]` | string | No | CFR section IDs |
| `conditions[topics][]` | string | No | Topic slugs |
| `conditions[significant]` | boolean | No | Filter for economically significant rules |
| `fields[]` | string (array) | No | Fields to include in response (see Field Reference below) |
| `per_page` | integer | No | Results per page (default: 20, max: 1000) |
| `page` | integer | No | Page number |
| `order` | string | No | Sort order: `relevance` (default), `newest`, `oldest`, `executive_order_number` |

#### Example Request - VA Rules

```
GET https://www.federalregister.gov/api/v1/documents.json
  ?conditions[agencies][]=veterans-affairs-department
  &conditions[type][]=RULE
  &conditions[publication_date][gte]=2025-01-01
  &fields[]=document_number
  &fields[]=title
  &fields[]=publication_date
  &fields[]=effective_on
  &fields[]=abstract
  &fields[]=html_url
  &fields[]=cfr_references
  &per_page=20
  &order=newest
```

Full URL form:
```
https://www.federalregister.gov/api/v1/documents.json?conditions%5Bagencies%5D%5B%5D=veterans-affairs-department&conditions%5Btype%5D%5B%5D=RULE&conditions%5Bpublication_date%5D%5Bgte%5D=2025-01-01&fields%5B%5D=document_number&fields%5B%5D=title&fields%5B%5D=publication_date&fields%5B%5D=effective_on&fields%5B%5D=abstract&fields%5B%5D=html_url&per_page=20&order=newest
```

#### Example Request - VA Proposed Rules

```
https://www.federalregister.gov/api/v1/documents.json?conditions%5Bagencies%5D%5B%5D=veterans-affairs-department&conditions%5Btype%5D%5B%5D=PRORULE&per_page=20&order=newest&fields%5B%5D=document_number&fields%5B%5D=title&fields%5B%5D=publication_date&fields%5B%5D=abstract&fields%5B%5D=html_url&fields%5B%5D=comments_close_on
```

#### Example Response

```json
{
  "count": 142,
  "description": "Search matching: ...",
  "total_pages": 8,
  "next_page_url": "https://www.federalregister.gov/api/v1/documents.json?page=2&...",
  "results": [
    {
      "document_number": "2024-14537",
      "title": "Agency Information Collection Activity: ...",
      "type": "NOTICE",
      "abstract": "...",
      "publication_date": "2024-07-02",
      "effective_on": null,
      "html_url": "https://www.federalregister.gov/documents/2024/07/02/2024-14537/...",
      "pdf_url": "https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14537.pdf",
      "citation": "89 FR 54962",
      "agency_names": ["Veterans Affairs Department"],
      "cfr_references": [{"title": 38, "part": 1}]
    }
  ]
}
```

---

### 2. Fetch Single Document

Retrieve full metadata for a specific document by its document number.

- **URL:** `GET /api/v1/documents/{document_number}.json`
- **Description:** Returns detailed metadata for a single Federal Register document.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `document_number` | string (path) | Yes | FR document number, e.g., `2024-14537` |
| `fields[]` | string (array) | No | Fields to include in response |

#### Example Request

```
GET https://www.federalregister.gov/api/v1/documents/2024-14537.json
```

#### Example Response

```json
{
  "document_number": "2024-14537",
  "title": "Agency Information Collection Activity: ...",
  "type": "NOTICE",
  "action": "Notice.",
  "abstract": "...",
  "dates": "Comments must be received on or before September 3, 2024.",
  "publication_date": "2024-07-02",
  "effective_on": null,
  "comments_close_on": "2024-09-03",
  "citation": "89 FR 54962",
  "start_page": 54962,
  "end_page": 54965,
  "page_length": 4,
  "volume": 89,
  "html_url": "https://www.federalregister.gov/documents/2024/07/02/2024-14537/...",
  "pdf_url": "https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14537.pdf",
  "full_text_xml_url": "https://www.govinfo.gov/content/pkg/FR-2024-07-02/xml/2024-14537.xml",
  "body_html_url": "https://www.federalregister.gov/documents/full_text/html/2024/2024-14537.htm",
  "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2024/2024-14537.txt",
  "json_url": "https://www.federalregister.gov/api/v1/documents/2024-14537.json",
  "agencies": [
    {
      "name": "Veterans Affairs Department",
      "id": 492,
      "url": "https://www.federalregister.gov/agencies/veterans-affairs-department",
      "json_url": "https://www.federalregister.gov/api/v1/agencies/492.json",
      "parent_id": null,
      "slug": "veterans-affairs-department"
    }
  ],
  "agency_names": ["Veterans Affairs Department"],
  "cfr_references": [{"title": 38, "part": 17}],
  "docket_ids": ["VA-2024-VHA-0001"],
  "regulation_id_numbers": ["2900-AQ27"],
  "significant": false
}
```

---

### 3. Fetch Multiple Documents

Retrieve metadata for multiple documents in a single request.

- **URL:** `GET /api/v1/documents/{document_numbers}.json`
- **Description:** Comma-separated list of document numbers.

#### Example Request

```
GET https://www.federalregister.gov/api/v1/documents/2024-14537,2024-10001.json
```

---

### 4. List Agencies

Retrieve information about all agencies or a specific agency.

- **URL:** `GET /api/v1/agencies.json`
- **URL (single):** `GET /api/v1/agencies/{id}.json`
- **Description:** Returns agency metadata including slugs needed for document filtering.

#### Example Request

```
GET https://www.federalregister.gov/api/v1/agencies.json
GET https://www.federalregister.gov/api/v1/agencies/492.json
```

#### Example Response (single agency)

```json
{
  "id": 492,
  "name": "Veterans Affairs Department",
  "short_name": "VA",
  "display_name": "Department of Veterans Affairs",
  "url": "https://www.federalregister.gov/agencies/veterans-affairs-department",
  "json_url": "https://www.federalregister.gov/api/v1/agencies/492.json",
  "logo": "...",
  "recent_articles_url": "https://www.federalregister.gov/api/v1/documents.json?conditions%5Bagencies%5D%5B%5D=veterans-affairs-department",
  "slug": "veterans-affairs-department",
  "parent_id": null
}
```

Key VA-related agencies and their slugs:
- `veterans-affairs-department` - Department of Veterans Affairs (ID: 492)
- `board-of-veterans-appeals` - Board of Veterans' Appeals
- `veterans-benefits-administration` - Veterans Benefits Administration

---

### 5. Public Inspection Documents (Current)

Documents filed with the OFR that will be published in the next Federal Register issue.

- **URL:** `GET /api/v1/public-inspection-documents/current.json`
- **Description:** Returns documents currently on public inspection (pre-publication).

#### Example Request

```
GET https://www.federalregister.gov/api/v1/public-inspection-documents/current.json
```

#### Example Response

```json
{
  "results": [
    {
      "document_number": "2025-07771",
      "title": "Agency Information Collection Activity: ...",
      "type": "NOTICE",
      "filing_type": "regular",
      "agencies": [{"name": "Veterans Affairs Department", "slug": "veterans-affairs-department"}],
      "filed_at": "2025-04-25T08:45:00.000-04:00",
      "publication_date": "2025-05-05",
      "pdf_url": "...",
      "html_url": "..."
    }
  ]
}
```

---

### 6. Public Inspection Documents (Search)

Search public inspection documents.

- **URL:** `GET /api/v1/public-inspection-documents.json`

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conditions[agencies][]` | string | No | Agency slug |
| `conditions[type][]` | string | No | Document type |
| `conditions[term]` | string | No | Full-text search |
| `conditions[available_on]` | string (YYYY-MM-DD) | No | Documents available on this date |
| `fields[]` | string | No | Fields to return |
| `per_page` | integer | No | Results per page |
| `page` | integer | No | Page number |
| `order` | string | No | Sort order |

---

### 7. Public Inspection Document by Number

- **URL:** `GET /api/v1/public-inspection-documents/{document_number}.json`

---

## Document Field Reference

Use `fields[]` parameters to select exactly which fields to return. Omitting `fields[]` returns a default minimal set.

### Core Identification
| Field | Type | Description |
|-------|------|-------------|
| `document_number` | string | FR document number (e.g., `2024-14537`) |
| `citation` | string | FR citation (e.g., `89 FR 54962`) |
| `title` | string | Document title |
| `type` | string | `RULE`, `PRORULE`, `NOTICE`, or `PRESDOCU` |
| `subtype` | string | Document subtype |
| `action` | string | Action text (e.g., "Final rule.") |

### Dates
| Field | Type | Description |
|-------|------|-------------|
| `publication_date` | string (YYYY-MM-DD) | Date published in FR |
| `effective_on` | string (YYYY-MM-DD) | Rule effective date |
| `signing_date` | string (YYYY-MM-DD) | Date signed by agency |
| `comments_close_on` | string (YYYY-MM-DD) | Comment period closing date |
| `dates` | string | Raw dates text from document |

### Content
| Field | Type | Description |
|-------|------|-------------|
| `abstract` | string | Document abstract/summary |
| `excerpts` | string | Search excerpt with highlighted terms |
| `start_page` | integer | Starting FR page number |
| `end_page` | integer | Ending FR page number |
| `page_length` | integer | Number of pages |
| `volume` | integer | FR volume number |

### URLs
| Field | Type | Description |
|-------|------|-------------|
| `html_url` | string | FederalRegister.gov document URL |
| `pdf_url` | string | Official PDF on govinfo.gov |
| `full_text_xml_url` | string | Full text XML |
| `body_html_url` | string | HTML rendition of document body |
| `raw_text_url` | string | Plain text version |
| `json_url` | string | This document's API URL |
| `mods_url` | string | MODS metadata XML |
| `abstract_html_url` | string | Abstract HTML |
| `public_inspection_pdf_url` | string | Pre-publication PDF |

### Agency
| Field | Type | Description |
|-------|------|-------------|
| `agencies` | array | Full agency objects (name, id, slug, parent_id) |
| `agency_names` | array | Agency name strings only |

### Regulatory Context
| Field | Type | Description |
|-------|------|-------------|
| `cfr_references` | array | CFR title/part references: `[{"title": 38, "part": 4}]` |
| `docket_id` | string | Primary docket ID |
| `docket_ids` | array | All docket IDs |
| `regulation_id_numbers` | array | RINs (e.g., `["2900-AQ27"]`) |
| `regulation_id_number_info` | object | RIN details from Unified Agenda |
| `regulations_dot_gov_info` | object | Regulations.gov metadata |
| `regulations_dot_gov_url` | string | Link to Regulations.gov docket |
| `significant` | boolean | Economically significant rule (EO 12866) |
| `topics` | array | Topic/CFR indexing terms |

### Presidential Documents
| Field | Type | Description |
|-------|------|-------------|
| `executive_order_number` | integer | EO number if applicable |
| `executive_order_notes` | string | EO notes |
| `president` | object | Signing president |

### Corrections
| Field | Type | Description |
|-------|------|-------------|
| `correction_of` | object | Document this corrects |
| `corrections` | array | Corrections to this document |

---

## Document Types

| Type Code | Description |
|-----------|-------------|
| `RULE` | Final Rules |
| `PRORULE` | Proposed Rules |
| `NOTICE` | Notices (most common; includes ICAs, SORNs, meetings) |
| `PRESDOCU` | Presidential Documents (EOs, proclamations) |

---

## VA-Specific Usage

### VA Agency Slug
The VA's agency slug for use in `conditions[agencies][]` is:
```
veterans-affairs-department
```

### Filtering by CFR Title 38
All VA regulations fall under Title 38 of the CFR. To filter:
```
conditions[cfr][title]=38
```

### Common VA Document Patterns

**Final rules (regulatory changes):**
```
GET /api/v1/documents.json?conditions[agencies][]=veterans-affairs-department&conditions[type][]=RULE&order=newest
```

**Proposed rules (comment opportunities):**
```
GET /api/v1/documents.json?conditions[agencies][]=veterans-affairs-department&conditions[type][]=PRORULE&order=newest
```

**All VA documents from a date range:**
```
GET /api/v1/documents.json
  ?conditions[agencies][]=veterans-affairs-department
  &conditions[publication_date][gte]=2025-01-01
  &conditions[publication_date][lte]=2025-12-31
  &per_page=100
  &order=newest
```

**VA documents affecting Title 38 CFR:**
```
GET /api/v1/documents.json
  ?conditions[agencies][]=veterans-affairs-department
  &conditions[cfr][title]=38
  &conditions[type][]=RULE
  &order=newest
```

**Search VA documents by keyword:**
```
GET /api/v1/documents.json
  ?conditions[agencies][]=veterans-affairs-department
  &conditions[term]=disability+rating
  &order=newest
```

---

## Python Integration Example

```python
import httpx

BASE_URL = "https://www.federalregister.gov/api/v1"

def search_va_documents(
    doc_types=None,
    date_gte=None,
    date_lte=None,
    term=None,
    per_page=20,
    page=1,
    order="newest"
):
    """
    Search VA Federal Register documents.

    doc_types: list of strings, e.g. ["RULE", "PRORULE", "NOTICE"]
    date_gte: string YYYY-MM-DD
    date_lte: string YYYY-MM-DD
    term: full-text search string
    """
    params = {
        "conditions[agencies][]": "veterans-affairs-department",
        "per_page": per_page,
        "page": page,
        "order": order,
        "fields[]": [
            "document_number",
            "title",
            "type",
            "publication_date",
            "effective_on",
            "abstract",
            "html_url",
            "pdf_url",
            "citation",
            "cfr_references",
            "docket_ids",
            "regulation_id_numbers",
            "comments_close_on",
        ],
    }

    if doc_types:
        params["conditions[type][]"] = doc_types
    if date_gte:
        params["conditions[publication_date][gte]"] = date_gte
    if date_lte:
        params["conditions[publication_date][lte]"] = date_lte
    if term:
        params["conditions[term]"] = term

    response = httpx.get(f"{BASE_URL}/documents.json", params=params)
    response.raise_for_status()
    return response.json()


def get_document(document_number):
    """Fetch a single document by number."""
    response = httpx.get(f"{BASE_URL}/documents/{document_number}.json")
    response.raise_for_status()
    return response.json()


def get_va_public_inspection():
    """Fetch VA documents currently on public inspection (pre-publication)."""
    params = {
        "conditions[agencies][]": "veterans-affairs-department",
        "fields[]": [
            "document_number",
            "title",
            "type",
            "filing_type",
            "publication_date",
            "agencies",
            "pdf_url",
        ],
    }
    response = httpx.get(f"{BASE_URL}/public-inspection-documents.json", params=params)
    response.raise_for_status()
    return response.json()


# Usage examples
if __name__ == "__main__":
    # Get recent VA final rules
    results = search_va_documents(doc_types=["RULE"], date_gte="2025-01-01")
    print(f"Found {results['count']} VA rules")

    # Get VA proposed rules with open comment periods
    proposals = search_va_documents(doc_types=["PRORULE"], order="newest")
    for doc in proposals["results"]:
        print(f"{doc['publication_date']} | {doc['title'][:80]}")
        if doc.get("comments_close_on"):
            print(f"  Comments close: {doc['comments_close_on']}")

    # Search for disability rating rules
    disability = search_va_documents(term="disability rating", doc_types=["RULE"])
    print(f"\nDisability rating rules: {disability['count']}")
```

---

## Pagination

Responses include:
- `count` - total number of matching documents
- `total_pages` - total pages available
- `next_page_url` - URL for the next page (null if on last page)
- `previous_page_url` - URL for the previous page

**Important:** You can only paginate through the first 2000 results. To access more, narrow your query using date range filters (`conditions[publication_date][gte]` and `conditions[publication_date][lte]`).

---

## Response Envelope

All search responses follow this structure:

```json
{
  "count": 500,
  "description": "Search criteria description",
  "total_pages": 25,
  "next_page_url": "https://...",
  "previous_page_url": null,
  "results": [ ... ]
}
```

---

## Error Handling

The API returns standard HTTP status codes:

| Status | Meaning |
|--------|---------|
| `200 OK` | Success |
| `400 Bad Request` | Invalid parameters |
| `404 Not Found` | Document number not found |
| `500 Internal Server Error` | Server error |

There are no documented rate limits. The API is public and has no throttling in practice, but reasonable request rates are expected.

---

## Rate Limits

No official rate limits are documented. The API is free and public. For bulk data needs, consider using the bulk XML downloads available via Data.gov rather than the API.

---

## Data Format Options

Append `.json` or `.csv` to endpoint paths:
- `.json` - JSON format (recommended)
- `.csv` - CSV format (limited fields)

---

## Additional Resources

- **Interactive API Explorer:** https://www.federalregister.gov/developers/documentation/api/v1
- **VA Agency Page:** https://www.federalregister.gov/agencies/veterans-affairs-department
- **VA Documents Search:** https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=veterans-affairs-department
- **GitHub (Ruby client):** https://github.com/usnationalarchives/federal_register
- **GitHub (API core):** https://github.com/usnationalarchives/federalregister-api-core
- **Bulk Data:** https://www.federalregister.gov/reader-aids/developer-resources/bulk-data
- **FR Index (by date):** https://www.federalregister.gov/index/{YYYY-MM-DD}.json

---

## Notes for BVA Integration

1. **VA agency slug** is `veterans-affairs-department` - confirmed from the live agency page.
2. **CFR Title 38** covers all VA benefits regulations. Use `conditions[cfr][title]=38` to narrow scope.
3. **Key document types** to monitor:
   - `RULE` - final regulatory changes (immediate impact on claims)
   - `PRORULE` - proposed rules (preview of upcoming changes, comment period open)
   - `NOTICE` - includes SORNs, ICAs, VA committee meetings
4. **Useful fields** for a BVA integration: `document_number`, `title`, `type`, `publication_date`, `effective_on`, `abstract`, `cfr_references`, `html_url`, `regulation_id_numbers`, `comments_close_on`
5. **No webhook/push support** - must poll periodically (recommend daily for new documents)
6. **Public inspection endpoint** gives 1-2 day preview of documents before they are officially published.
