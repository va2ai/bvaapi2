#!/usr/bin/env bash
#
# Bootstrap GCP project for Cloud Run + Artifact Registry + Cloud Build
# Usage: ./bootstrap.sh <PROJECT_ID> [REGION]
#
# Example:
#   ./bootstrap.sh my-gcp-project us-central1
#

set -euo pipefail

PROJECT_ID="${1:-}"
REGION="${2:-us-central1}"   # default region if not supplied
REPO_NAME="bva-api"          # docker repo name
SERVICE_NAME="bva-api"       # cloud run service name

if [[ -z "$PROJECT_ID" ]]; then
  echo "Usage: $0 <PROJECT_ID> [REGION]" >&2
  exit 1
fi

echo "Bootstrapping GCP project:"
echo "  Project ID : $PROJECT_ID"
echo "  Region     : $REGION"
echo "  Repo name  : $REPO_NAME"
echo "  Service    : $SERVICE_NAME"
echo

# Set project
gcloud config set project "$PROJECT_ID"

# Enable required services
echo "Enabling APIs..."
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com \
  logging.googleapis.com \
  monitoring.googleapis.com

# Create Artifact Registry for Docker images
echo "Creating Artifact Registry (if not exists)..."
gcloud artifacts repositories create "$REPO_NAME" \
  --repository-format=docker \
  --location="$REGION" \
  --description="Container images for $SERVICE_NAME" \
  --quiet || echo "Repository may already exist, continuing..."

# (Optional) create a service account for Cloud Build/Run
# gcloud iam service-accounts create cloud-run-builder \
#     --display-name "Cloud Run Builder"

echo "Bootstrap complete."
echo "Next steps:"
echo "  1. Commit a cloudbuild.yaml to your repo."
echo "  2. Deploy with: gcloud builds submit --substitutions=_REGION=${REGION},_REPO=${REPO_NAME},_SERVICE=${SERVICE_NAME}"
echo "  3. Update your client base_url to the Cloud Run URL after deploy."
