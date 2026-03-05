# Stage 6 — MLOps & AI Deployment

## 🎯 Learning Objectives

By the end of this stage you will:
- Deploy ML models as REST APIs with FastAPI
- Containerize AI applications with Docker
- Set up CI/CD pipelines for AI projects
- Track experiments with MLflow
- Monitor models in production
- Scale AI applications on cloud platforms

## ⏱️ Estimated Time: 2 weeks

---

## 📐 Key Concepts

### 1. Model Serving

| Approach | Tool | Best For |
|----------|------|---------|
| REST API | FastAPI | Custom serving, control |
| BentoML | BentoML | Easy production packaging |
| TorchServe | PyTorch | PyTorch model serving |
| TF Serving | TensorFlow | TF models at scale |
| vLLM | vLLM | High-throughput LLM serving |
| Triton | NVIDIA Triton | GPU-optimized serving |

### 2. FastAPI for AI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: PredictRequest):
    result = model.predict(request.text)
    return {"prediction": result}
```

### 3. Docker for AI Applications

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 4. Experiment Tracking with MLflow

- Log parameters, metrics, and artifacts
- Compare runs visually
- Register and version models
- Serve models directly from MLflow

### 5. CI/CD for AI

```yaml
# GitHub Actions workflow
name: AI Model CI/CD
on: [push]
jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest tests/
      - name: Build Docker image
        run: docker build -t ai-app .
      - name: Deploy to cloud
        run: # your deploy commands
```

### 6. Model Monitoring

- **Data drift** — Input distribution shift over time
- **Concept drift** — Model accuracy degradation
- **Latency monitoring** — P50, P95, P99 response times
- **Error rates** — Track prediction failures
- **Tools:** Evidently AI, Arize AI, WhyLogs

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| FastAPI | API development |
| Uvicorn | ASGI server |
| Docker | Containerization |
| Docker Compose | Multi-service apps |
| MLflow | Experiment tracking |
| GitHub Actions | CI/CD |
| AWS EC2 / GCP Compute | Cloud compute |
| AWS Lambda | Serverless inference |
| Modal | Serverless GPU functions |
| Evidently AI | Model monitoring |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| FastAPI Docs | Official | https://fastapi.tiangolo.com/ |
| Docker for Data Scientists | YouTube | https://www.youtube.com/watch?v=0qG_0CPB_eE |
| MLflow Docs | Official | https://mlflow.org/docs/latest/index.html |
| Made With ML — MLOps Course | Free Course | https://madewithml.com/ |
| Full Stack Deep Learning | Free Course | https://fullstackdeeplearning.com/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_fastapi_model_serving.ipynb` — Serve a Scikit-learn model with FastAPI
- `02_docker_containerization.md` — Step-by-step Docker tutorial
- `03_mlflow_tracking.ipynb` — Log and compare ML experiments
- `04_github_actions_ci.md` — Set up CI/CD for your AI project

---

## 🛠️ Mini Projects

1. **Model API** — Wrap any trained model in a FastAPI endpoint with proper input validation
2. **Docker Compose Stack** — A multi-service app: FastAPI + Streamlit + PostgreSQL
3. **Experiment Dashboard** — MLflow tracking for 5+ model variants

---

## 🏆 Major Project

### End-to-End MLOps Pipeline

Build a complete production-ready AI system:

**Services:**
- **FastAPI** — Prediction API with authentication
- **Streamlit** — User interface
- **MLflow** — Experiment tracking and model registry
- **PostgreSQL** — Prediction logging
- **Docker Compose** — Orchestrate all services

**CI/CD Pipeline (GitHub Actions):**
1. Run tests
2. Build Docker images
3. Push to Docker Hub
4. Deploy to cloud VM

**Monitoring:**
- Log every prediction to database
- Track model accuracy on live data
- Send alerts if accuracy drops below threshold

See [projects/mlops-pipeline/](./projects/) for the full template.

---

## ✅ Stage Completion Checklist

- [ ] Built and tested a FastAPI model serving endpoint
- [ ] Containerized an AI app with Docker
- [ ] Set up MLflow experiment tracking
- [ ] Created a GitHub Actions CI/CD pipeline
- [ ] Deployed a model to a cloud platform (AWS/GCP/Modal)
- [ ] Pushed the complete MLOps project to GitHub

**Next Stage → [07 AI Projects](../07-ai-projects/)**
