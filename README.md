# BVA Decision Scraper API

A high-performance FastAPI service for searching and analyzing Board of Veterans' Appeals (BVA) decisions. This API provides real-time access to BVA decisions without requiring a database, utilizing the USA.gov search API and web scraping.

## 🚀 Features

- **Real-time BVA Decision Search**: Search through thousands of BVA decisions by query and year
- **Case Detail Extraction**: Parse and extract structured data from decision texts
- **Batch Operations**: Search multiple queries simultaneously
- **Text Analysis**: Analyze decisions for keywords, VA-specific terms, and readability metrics
- **No Database Required**: Direct scraping and parsing without persistence layer
- **Rate-Limited & Optimized**: Built-in rate limiting and concurrent request handling
- **Cloud-Ready**: Dockerized with GCP Cloud Run deployment support

## 📋 Table of Contents

- [API Endpoints](#api-endpoints)
- [Quick Start](#quick-start)
- [Local Development](#local-development)
- [GCP Deployment](#gcp-deployment)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and available endpoints |
| `/search` | POST | Search BVA decisions with pagination |
| `/case` | GET | Fetch detailed case information |
| `/case/text` | GET | Get raw text of a specific case |
| `/batch/search` | POST | Search multiple queries in batch |
| `/analyze/text` | GET | Analyze decision text for keywords and metrics |
| `/health` | GET | Health check endpoint |

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker (for containerized deployment)
- Google Cloud SDK (for GCP deployment)
- Active GCP Project (for cloud deployment)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/ccdmndkut/bvaapi.git
cd bvaapi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:8001`

## 💻 Local Development

### Running with Docker

1. Build the Docker image:
```bash
docker build -t bva-api .
```

2. Run the container:
```bash
docker run -p 8080:8080 bva-api
```

### Development with Live Reload

For development with automatic reload on code changes:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8001
```

### Testing the API

Visit the interactive API documentation at:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## ☁️ GCP Deployment

### Prerequisites

1. Install Google Cloud SDK:
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

2. Initialize gcloud and authenticate:
```bash
gcloud init
gcloud auth login
```

### Deployment Steps

#### 1. Bootstrap GCP Project

Run the bootstrap script to configure your GCP project:

```bash
chmod +x bootstrap.sh
./bootstrap.sh optimal-transit-472305-v7 us-central1
```

This script will:
- Enable required GCP APIs (Cloud Run, Artifact Registry, Cloud Build, etc.)
- Create an Artifact Registry repository for Docker images
- Configure project settings

#### 2. Deploy Using Cloud Build

Deploy the application using Cloud Build:

**Linux/Mac:**
```bash
gcloud builds submit --config=cloudbuild.yaml \
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

**Windows (Command Prompt):**
```cmd
gcloud builds submit --config=cloudbuild.yaml ^
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

**Windows (PowerShell):**
```powershell
gcloud builds submit --config=cloudbuild.yaml `
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

This will:
- Build the Docker image
- Push it to Artifact Registry
- Deploy to Cloud Run with automatic HTTPS

**⚠️ Troubleshooting Cloud Build Permissions**

If you encounter an error like:
```
ERROR: (gcloud.builds.submit) The user is forbidden from accessing the bucket [PROJECT_ID_cloudbuild]
```

This is a common permissions issue. Here are the solutions:

**Solution 1: Set the correct project (Recommended)**
```bash
# Ensure you're using the correct project
gcloud config set project optimal-transit-472305-v7

# Verify the project is set
gcloud config get-value project
```

**Solution 2: Grant necessary permissions**
```bash
# Get your current user email
gcloud config get-value account

# Grant Cloud Build Editor role
gcloud projects add-iam-policy-binding optimal-transit-472305-v7 \
  --member="user:YOUR_EMAIL@gmail.com" \
  --role="roles/cloudbuild.builds.editor"

# Grant Service Usage Admin role (if needed)
gcloud projects add-iam-policy-binding optimal-transit-472305-v7 \
  --member="user:YOUR_EMAIL@gmail.com" \
  --role="roles/serviceusage.serviceUsageAdmin"
```

**Solution 3: Create Cloud Storage bucket manually**
```bash
# Create the Cloud Build staging bucket
gsutil mb -p optimal-transit-472305-v7 gs://optimal-transit-472305-v7_cloudbuild/

# Grant your user access to the bucket
gsutil iam ch user:YOUR_EMAIL@gmail.com:objectAdmin \
  gs://optimal-transit-472305-v7_cloudbuild/
```

**Solution 4: Use local build alternative**
If permissions issues persist, use the manual Docker build and deploy method described in the "Manual Deployment Alternative" section below.

#### 3. Get Your API URL

After deployment, get your Cloud Run service URL:

```bash
gcloud run services describe bva-api --region=us-central1 --format='value(status.url)'
```

### Updating an Existing Deployment

After your initial deployment, updating the API is streamlined:

#### Option 1: Using Cloud Build (Recommended)

Simply run the same Cloud Build command - it will automatically rebuild and redeploy:

**Linux/Mac:**
```bash
gcloud builds submit --config=cloudbuild.yaml \
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

**Windows (Command Prompt):**
```cmd
gcloud builds submit --config=cloudbuild.yaml ^
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

**Windows (PowerShell):**
```powershell
gcloud builds submit --config=cloudbuild.yaml `
  --substitutions=_REGION=us-central1,_REPO=bva-api,_SERVICE=bva-api
```

This command will:
1. Build a new Docker image with your latest code changes
2. Push the updated image to Artifact Registry (overwrites the `latest` tag)
3. Automatically update the Cloud Run service with the new image
4. Perform a rolling deployment with zero downtime

#### Option 2: Manual Update Process

If you need more control over the update process:

1. **Rebuild and push the Docker image:**
```bash
# Rebuild with your changes
docker build -t us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest .

# Push the updated image
docker push us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest
```

2. **Update the Cloud Run service:**

**Linux/Mac:**
```bash
gcloud run deploy bva-api \
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest \
  --region us-central1
```

**Windows (Command Prompt):**
```cmd
gcloud run deploy bva-api ^
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest ^
  --region us-central1
```

**Windows (PowerShell):**
```powershell
gcloud run deploy bva-api `
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest `
  --region us-central1
```

#### Option 3: Using Versioned Images

For better version control and rollback capabilities:

1. **Build with a version tag:**
```bash
# Use semantic versioning or timestamps
VERSION=v1.1.1  # or $(date +%Y%m%d-%H%M%S)

docker build -t us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:${VERSION} .
docker push us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:${VERSION}

# Also update latest (Linux/Mac)
docker tag us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:${VERSION} \
  us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest

# Windows Command Prompt
docker tag us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:%VERSION% ^
  us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest

# Windows PowerShell
docker tag us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:$env:VERSION `
  us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest
docker push us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest
```

2. **Deploy the specific version:**

**Linux/Mac:**
```bash
gcloud run deploy bva-api \
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:${VERSION} \
  --region us-central1
```

**Windows (Command Prompt):**
```cmd
gcloud run deploy bva-api ^
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:%VERSION% ^
  --region us-central1
```

**Windows (PowerShell):**
```powershell
gcloud run deploy bva-api `
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:$env:VERSION `
  --region us-central1
```

#### Rollback to Previous Version

If you need to rollback to a previous version:

```bash
# List available revisions
gcloud run revisions list --service bva-api --region us-central1

# Rollback to a specific revision (Linux/Mac)
gcloud run services update-traffic bva-api \
  --to-revisions=bva-api-00002-abc=100 \
  --region us-central1

# Windows Command Prompt
gcloud run services update-traffic bva-api ^
  --to-revisions=bva-api-00002-abc=100 ^
  --region us-central1

# Windows PowerShell
gcloud run services update-traffic bva-api `
  --to-revisions=bva-api-00002-abc=100 `
  --region us-central1
```

#### Update Best Practices

1. **Test Locally First**: Always test changes locally before deploying
   ```bash
   docker build -t bva-api-test .
   docker run -p 8080:8080 bva-api-test
   ```

2. **Use Blue-Green Deployments**: For critical updates, deploy to a staging service first
   
   **Linux/Mac:**
   ```bash
   gcloud run deploy bva-api-staging \
     --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest \
     --region us-central1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   gcloud run deploy bva-api-staging ^
     --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest ^
     --region us-central1
   ```
   
   **Windows (PowerShell):**
   ```powershell
   gcloud run deploy bva-api-staging `
     --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest `
     --region us-central1
   ```

3. **Monitor Deployment**: Watch the deployment progress
   ```bash
   gcloud run services describe bva-api --region us-central1 --format='value(status.conditions[0].message)'
   ```

4. **Check Logs After Deployment**: Verify the new version is running correctly
   
   **Linux/Mac:**
   ```bash
   gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=bva-api" \
     --limit 50 --format json
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=bva-api" ^
     --limit 50 --format json
   ```
   
   **Windows (PowerShell):**
   ```powershell
   gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=bva-api" `
     --limit 50 --format json
   ```

### Manual Deployment Alternative

If you prefer manual deployment:

1. Build and push Docker image:
```bash
# Configure Docker for Artifact Registry
gcloud auth configure-docker us-central1-docker.pkg.dev

# Build image
docker build -t us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest .

# Push to registry
docker push us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest
```

2. Deploy to Cloud Run:

**Linux/Mac:**
```bash
gcloud run deploy bva-api \
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 1Gi \
  --cpu 1 \
  --timeout 300 \
  --max-instances 10
```

**Windows (Command Prompt):**
```cmd
gcloud run deploy bva-api ^
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest ^
  --region us-central1 ^
  --allow-unauthenticated ^
  --port 8080 ^
  --memory 1Gi ^
  --cpu 1 ^
  --timeout 300 ^
  --max-instances 10
```

**Windows (PowerShell):**
```powershell
gcloud run deploy bva-api `
  --image us-central1-docker.pkg.dev/optimal-transit-472305-v7/bva-api/bva-api:latest `
  --region us-central1 `
  --allow-unauthenticated `
  --port 8080 `
  --memory 1Gi `
  --cpu 1 `
  --timeout 300 `
  --max-instances 10
```

## 📖 API Documentation

### Search Decisions

**Endpoint:** `POST /search`

**Request Body:**
```json
{
  "query": "PTSD combat veteran",
  "year": 2024,
  "max_pages": 3,
  "page_size": 20
}
```

**Response:**
```json
{
  "query": "PTSD combat veteran",
  "total_results": 60,
  "pages_searched": 3,
  "results": [
    {
      "url": "https://www.va.gov/vetapp24/files/24001234.txt",
      "title": "Citation Nr: 24001234",
      "snippet": "PTSD with combat stressors...",
      "year": 2024,
      "case_number": "24001234"
    }
  ],
  "timestamp": "2025-09-22T10:30:00"
}
```

### Get Case Details

**Endpoint:** `GET /case?url=<case_url>&full_text=false`

**Response:**
```json
{
  "url": "https://www.va.gov/vetapp24/files/24001234.txt",
  "year": 2024,
  "case_number": "24001234",
  "docket_no": "23-12345",
  "decision_date": "2024-01-15",
  "outcome": "Granted",
  "judge": "John Smith",
  "regional_office": "Houston",
  "issues": ["PTSD", "Hearing Loss"],
  "citations": ["38 CFR § 3.304", "38 CFR § 4.130"],
  "text_length": 15234,
  "text_preview": "Decision text preview...",
  "fetch_timestamp": "2025-09-22T10:30:00"
}
```

### Batch Search

**Endpoint:** `POST /batch/search`

**Request Body:**
```json
{
  "queries": ["PTSD", "TBI", "hearing loss"],
  "year": 2024,
  "max_pages": 2
}
```

### Text Analysis

**Endpoint:** `GET /analyze/text?url=<case_url>&keywords=PTSD,combat&context=true`

**Response:**
```json
{
  "url": "https://www.va.gov/vetapp24/files/24001234.txt",
  "case_number": "24001234",
  "text_length": 15234,
  "keyword_counts": {
    "PTSD": 12,
    "combat": 5
  },
  "keyword_contexts": {
    "PTSD": ["...diagnosed with PTSD following combat...", "...service-connected PTSD symptoms..."]
  },
  "va_terms_found": {
    "TDIU": 0,
    "PTSD": 12,
    "service-connected": 8,
    "disability rating": 3
  },
  "readability_grade": 14.5,
  "analysis_timestamp": "2025-09-22T10:30:00"
}
```

## ⚙️ Configuration

### Environment Variables

The application uses the following environment variables (set in Dockerfile):

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 8080 | Server port |
| `UVICORN_WORKERS` | 2 | Number of worker processes |
| `UVICORN_TIMEOUT` | 120 | Request timeout in seconds |

### Rate Limiting

- Default delay between requests: 2 seconds
- Maximum pages per search: 20
- Concurrent request workers: 10

### Year-to-DC Mapping

The API includes a comprehensive year-to-DC mapping (1997-2025) for accurate year-based filtering in the USA.gov search API.

## 🏗️ Architecture

### Technology Stack

- **Framework**: FastAPI 0.115.0
- **ASGI Server**: Uvicorn 0.30.6
- **Web Scraping**: BeautifulSoup4, Requests
- **Text Analysis**: textstat
- **Containerization**: Docker
- **Cloud Platform**: Google Cloud Platform
  - Cloud Run (serverless container hosting)
  - Artifact Registry (container registry)
  - Cloud Build (CI/CD)

### Project Structure

```
bvaapi/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── cloudbuild.yaml    # GCP Cloud Build configuration
├── bootstrap.sh       # GCP project setup script
└── README.md         # This file
```

### Data Flow

1. **Client Request** → FastAPI endpoint
2. **Query Building** → Construct USA.gov search URL with parameters
3. **Web Scraping** → Fetch and parse search results
4. **Data Extraction** → Parse decision text using regex patterns
5. **Response Formation** → Structure data into Pydantic models
6. **JSON Response** → Return to client

## 🔒 Security Considerations

- **No Authentication**: Currently deployed with `--allow-unauthenticated`. Consider adding authentication for production.
- **Rate Limiting**: Built-in delays to prevent overwhelming source servers
- **Input Validation**: Pydantic models validate all inputs
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is provided as-is for educational and research purposes. Please ensure compliance with VA.gov terms of service when using this API.

## 🆘 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/ccdmndkut/bvaapi/issues).

## 🔄 Version History

- **v1.1.0** (Current)
  - Optimized text analysis with single-pass keyword scanning
  - Enhanced year-to-DC mapping (1997-2025)
  - Improved error handling and logging
  
- **v1.0.1**
  - Added readability analysis using Flesch-Kincaid grade
  - Improved Pydantic models for structured request handling
  - Enhanced logging and error handling

- **v1.0.0**
  - Initial release with core functionality
  - Search, case retrieval, and batch operations
  - Docker support and GCP deployment configuration

---

**Note**: This API scrapes publicly available BVA decisions. Please use responsibly and in accordance with all applicable laws and terms of service.
