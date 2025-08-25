 # Disease Outbreak Predictor #
 Predicts region‑level outbreak risk using environmental and health indicators, with a REST API for real‑time and batch inference and an optional dashboard for visualizing hot‑spots.

Model: scikit‑learn (classification)

API: FastAPI (JSON, OpenAPI docs)

Data: CSV/Parquet with features like weather, demographics, historical cases

Optional UI: Minimal dashboard or React client

Demo

API docs: http://localhost:8000/docs

Health check: http://localhost:8000/health

Optional UI: http://localhost:5173 (if you add a frontend)

Features

Supervised classification to assign risk tiers (Low/Medium/High)

Feature engineering (lags, rolling stats, scaling/encoding)

Robust evaluation (ROC‑AUC, PR‑AUC, F1, calibration)

Batch and real‑time inference endpoints

Input validation with Pydantic

Dockerized for reproducible runs

Optional persistence of predictions for auditability

Table of Contents

Project structure

Quick start

Data

Training

Evaluation

Serving (API)

Examples

Deployment

Monitoring & Logging

Roadmap

Tech stack

License

Project structure
.
├─ data/
│ ├─ raw/
│ ├─ processed/
├─ models/
│ └─ model.pkl
├─ notebooks/
│ └─ EDA_YYYYMM.ipynb
├─ src/
│ ├─ features.py
│ ├─ train.py
│ ├─ evaluate.py
│ ├─ schema.py
│ ├─ service.py # FastAPI app
│ ├─ utils.py
│ └─ config.py
├─ tests/
│ ├─ test_features.py
│ └─ test_api.py
├─ requirements.txt / pyproject.toml
├─ Dockerfile
├─ docker-compose.yml
├─ Makefile
└─ README.md

Quick start

Clone and set up

git clone https://github.com/YOUR_USERNAME/disease-outbreak-predictor.git

cd disease-outbreak-predictor

python -m venv .venv && source .venv/bin/activate # or use uv/poetry

pip install -r requirements.txt

Environment variables
Create a .env file:

DATA_DIR=./data/processed

MODEL_PATH=./models/model.pkl

LOG_LEVEL=INFO

SAVE_PREDICTIONS=false

DB_URL=postgresql://USER:PASSWORD@HOST:5432/DBNAME # optional

Run API

uvicorn src.service:app --reload --port 8000

Open http://localhost:8000/docs

Optional: Docker

docker compose up --build

API at http://localhost:8000

Data

Description: Historical disease cases by region and time, with environmental and demographic features.

Example fields:

date, region_id, region_name

historical_cases, population_density

temp_avg, humidity_avg, rainfall_mm

lag_7_cases, rolling_14_cases

Source: YOUR_SOURCE_NAME (link or description)

Privacy note: Only public and anonymized data used.

Training

Preprocessing: handle missing values, feature scaling/encoding, lag/rolling windows

Models tried: Logistic Regression, Random Forest, XGBoost

Selection criteria: ROC‑AUC/F1 on time‑aware splits; calibration checked

Command line:

python src/train.py --data data/processed/dataset.csv --out models/model.pkl --model xgboost

Parameters: --threshold 0.5 --cv 5 --seed 42

Evaluation

Metrics: ROC‑AUC, PR‑AUC, F1, precision/recall, calibration error

Plots saved to ./reports:

ROC, PR curves

Calibration curve

Feature importance (when applicable)

Command line:

python src/evaluate.py --data data/processed/holdout.csv --model models/model.pkl --report ./reports

Serving (API)

Stack: FastAPI + Pydantic

Start:

uvicorn src.service:app --host 0.0.0.0 --port 8000

Endpoints:

GET /health — service status

GET /version — model metadata

POST /predict — single prediction

POST /predict-batch — multiple predictions

Request schemas (simplified):
{
"region_id": "R123",
"date": "2025-01-05",
"temp_avg": 29.4,
"humidity_avg": 71.2,
"rainfall_mm": 12.5,
"historical_cases": 14,
"population_density": 5600,
"lag_7_cases": 9,
"rolling_14_cases": 11.3
}

Response (example):
{
"region_id": "R123",
"risk_score": 0.78,
"risk_tier": "High",
"model_version": "2025.01.x",
"timestamp": "2025-01-05T12:00:00Z"
}

Examples

Single predict:
curl -X POST http://localhost:8000/predict
-H "Content-Type: application/json"
-d '{"region_id":"R123","date":"2025-01-05","temp_avg":29.4,"humidity_avg":71.2,"rainfall_mm":12.5,"historical_cases":14,"population_density":5600,"lag_7_cases":9,"rolling_14_cases":11.3}'

Batch predict:
curl -X POST http://localhost:8000/predict-batch
-H "Content-Type: application/json"
-d '{"items":[{...},{...}]}'

Deployment

Docker: docker compose up --build

Render/Fly.io: deploy the API container; set env vars and persistent volume for models

Optional: Nginx reverse proxy; enable gzip and caching for /static

Optional: CI/CD via GitHub Actions to run tests and build images on PRs/tags

Monitoring & Logging

Structured logs (JSON) with request_id per call

Basic metrics: request counts, latency percentiles, error rates

Health checks: /health, and readiness/liveness if on Kubernetes

Roadmap

Add calibration diagnostics to API metadata

Add geo visualization (Folium/Leaflet) for hot‑spots map

Persist predictions to PostgreSQL with simple audit trail

JWT auth for restricted endpoints

Add model registry/versioning hooks (MLflow)

Tech stack

Python, scikit‑learn, Pandas, NumPy

FastAPI, Pydantic, Uvicorn

PostgreSQL (optional persistence), SQLAlchemy (optional)

Docker, Makefile, GitHub Actions (optional)

Contributing

PRs welcome. Please open an issue first to discuss major changes.

Run tests and lints before submitting:

pytest -q

ruff check . # or flake8/black if you use them

License

MIT (or your preferred license). See LICENSE.

Acknowledgments

Data sources: YOUR_SOURCE_NAME

Inspiration: public health risk modeling literature and open datasets

Badges (optional)
Add GitHub Actions, Docker, or license badges at the top once configured.

Notes for your repo

Include a small sample in data/processed/sample.csv for quick API tests.

Add OpenAPI examples in src/schema.py so /docs shows realistic payloads.

If you add a frontend, document npm/yarn dev commands and environment variables in a separate CLIENT.md.
