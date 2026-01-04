#!/bin/bash
set -e

echo "Initializing Sentinel Platform Environment..."

# 1. Python Virtual Environment Setup
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r sentinel/requirements.txt
pip install -r tests/requirements-dev.txt

# 2. Infrastructure Initialization
echo "cloud: Azure" > .env
cd infra/terraform
terraform init -backend=false # Validate local config
cd ../..

# 3. Pre-commit Hooks (Ensures code quality before every git commit)
pip install pre-commit
pre-commit install

# 4. Create Mock Data for Local Testing
mkdir -p tests/data
python scripts/simulation/generate_mock_bc_data.py

echo "Environment Ready. Use 'source venv/bin/activate' to start."
