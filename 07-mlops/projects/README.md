# End-to-End MLOps Pipeline

A complete, production-ready AI system with model serving, monitoring, and CI/CD.

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Streamlit  │────▶│   FastAPI   │────▶│  ML Model   │
│     UI      │     │     API     │     │  (joblib)   │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    ┌──────▼──────┐     ┌─────────────┐
                    │ PostgreSQL  │     │   MLflow    │
                    │  (logging)  │     │  (tracking) │
                    └─────────────┘     └─────────────┘
```

## 🚀 Getting Started

```bash
# Clone and set up
git clone <your-repo>
cd mlops-pipeline

# Start all services
docker compose up --build

# Access:
# Streamlit UI:    http://localhost:8501
# FastAPI docs:    http://localhost:8000/docs
# MLflow UI:       http://localhost:5000
```

## 📁 Project Structure

```
mlops-pipeline/
├── api/
│   ├── main.py              # FastAPI app
│   ├── models.py            # Pydantic schemas
│   └── Dockerfile
├── frontend/
│   ├── app.py               # Streamlit UI
│   └── Dockerfile
├── ml/
│   ├── train.py             # Training script
│   ├── evaluate.py          # Evaluation
│   └── model.pkl            # Saved model
├── monitoring/
│   └── dashboard.py         # Monitoring dashboard
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions
├── docker-compose.yml
└── requirements.txt
```

## 🔄 CI/CD Pipeline

```yaml
name: AI App CI/CD
on: push

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build and push Docker image
        run: docker build -t my-ai-app . && docker push my-ai-app
```
