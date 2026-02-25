# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080 \
    UVICORN_WORKERS=2 \
    UVICORN_TIMEOUT=120 \
    BVA_API_URL=http://localhost:8080

# System deps (certs, build tools for wheels if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# If you have private libs, copy and install first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# If you need environment config, read from env/Secret Manager at runtime
# Expose port (Cloud Run honors $PORT)
EXPOSE 8080

# Healthcheck (works locally and in many container runtimes)
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -fsS http://127.0.0.1:${PORT}/health || exit 1

# Start FastAPI via uvicorn (configure host/port, workers via env)
CMD exec uvicorn app:app --host 0.0.0.0 --port ${PORT} --workers ${UVICORN_WORKERS}
