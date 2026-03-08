# Repository Guidelines

## Project Structure & Module Organization
This repository is a Python FastAPI service with an optional MCP wrapper.

- `app.py`: main API application and route definitions.
- `cavc_client.py`: CAVC eFiling integration logic.
- `mcp_server.py`: MCP tool server that calls the HTTP API.
- `rag.py`, `ingest.py`, `chunker.py`: retrieval/indexing utilities.
- `docs/`: supporting technical notes.
- `logs/`: runtime logs (local only; do not commit).
- `test_knowva.py`: API smoke-style test script.

Note: files with names like `* (2).*` are legacy duplicates and should generally not be used for new changes.

## Build, Test, and Development Commands
- `pip install -r requirements.txt`: install runtime dependencies.
- `python app.py`: run API locally (default port `8001`).
- `uvicorn app:app --reload --host 0.0.0.0 --port 8001`: run with live reload for development.
- `python mcp_server.py`: start MCP server (`stdio` by default; set `MCP_TRANSPORT=http` for HTTP mode).
- `pytest -q`: run tests.
- `pytest -q test_knowva.py -s`: run the KnowVA smoke test with console output.
- `docker build -t bva-api . && docker run -p 8080:8080 bva-api`: containerized local run.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation.
- Use `snake_case` for functions/variables, `PascalCase` for Pydantic models/classes, and `UPPER_SNAKE_CASE` for constants.
- Prefer explicit type hints (`Optional`, `List`, `Dict`, etc.) on public functions and models.
- Keep route handlers thin; move reusable parsing/client logic into helper modules.
- Preserve existing logging style (`logging` with structured, concise messages).

## Testing Guidelines
- Framework: `pytest`.
- Test files: `test_*.py`; test functions: `test_*`.
- Add tests for new endpoints, validation branches, and error responses.
- For integrations (external APIs), prefer smoke tests with clear skips/fail reasons over brittle assertions.

## Commit & Pull Request Guidelines
- Follow Conventional Commit style seen in history: `feat: ...`, `fix: ...`, `docs: ...`.
- Keep commits scoped to a single change and include API-impact details when relevant.
- PRs should include:
  - What changed and why.
  - A short verification section (commands run, sample endpoint calls).
  - Any OpenAPI or behavior changes (and updated docs/examples).

## Security & Configuration Tips
- Use environment variables for runtime settings (`PORT`, `UVICORN_WORKERS`, `UVICORN_TIMEOUT`, `BVA_API_URL`, `MCP_TRANSPORT`).
- Never commit secrets, `.env` files, or generated local data under `logs/` or `data/`.
