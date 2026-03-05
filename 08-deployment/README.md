# Stage 8 — AI Deployment & Infrastructure

## 🎯 Learning Objectives

By the end of this stage you will:
- Deploy AI models and LLM applications to cloud platforms (AWS, GCP, Azure)
- Containerize and orchestrate AI services with Docker and Kubernetes
- Optimize inference performance with quantization, batching, and caching
- Serve LLMs at scale using vLLM, TGI, and other high-throughput engines
- Deploy serverless AI workloads on Modal, AWS Lambda, and Google Cloud Functions
- Implement AI observability and monitoring with Langfuse, Langsmith, Arize, and Evidently
- Build AI evaluation pipelines to measure quality, cost, and latency in production
- Apply AI security best practices — prompt injection defense, guardrails, and data privacy
- Design cost-optimized AI architectures with API gateways, rate limiting, and caching
- Build and ship end-to-end AI products with auth, payments, and production infrastructure

## ⏱️ Estimated Time: 2 weeks

---

## 📐 Key Concepts

### 1. Cloud Deployment for AI

The three major cloud providers each offer AI-specific services alongside general compute:

| Provider | Compute | AI/ML Service | Serverless | Container Orchestration |
|----------|---------|---------------|------------|------------------------|
| AWS | EC2 (GPU instances) | SageMaker | Lambda | EKS (Kubernetes) |
| GCP | Compute Engine (GPU) | Vertex AI | Cloud Functions | GKE (Kubernetes) |
| Azure | Virtual Machines (GPU) | Azure ML | Azure Functions | AKS (Kubernetes) |

**Typical AI Deployment Architecture:**

```
Client Request
     ↓
┌──────────────────┐
│   API Gateway     │ ← Rate limiting, auth, routing
│  (Kong / AWS ALB) │
└──────────────────┘
     ↓
┌──────────────────┐
│  Load Balancer    │ ← Distribute across replicas
└──────────────────┘
     ↓
┌──────────────────────────────────────┐
│       AI Service Replicas            │
│  ┌─────────┐ ┌─────────┐ ┌────────┐ │
│  │ GPU Pod │ │ GPU Pod │ │GPU Pod │ │
│  │ (vLLM)  │ │ (vLLM)  │ │(vLLM)  │ │
│  └─────────┘ └─────────┘ └────────┘ │
└──────────────────────────────────────┘
     ↓
┌──────────────────┐
│   Cache Layer     │ ← Redis / semantic cache
│   Monitoring      │ ← Langfuse / Arize
│   Logging         │ ← Structured prediction logs
└──────────────────┘
```

### 2. Docker & Kubernetes for AI

**Production Dockerfile for an AI Service:**

```dockerfile
FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Kubernetes Deployment for an AI Service:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-inference-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-inference
  template:
    metadata:
      labels:
        app: ai-inference
    spec:
      containers:
      - name: ai-inference
        image: your-registry/ai-service:latest
        ports:
        - containerPort: 8000
        resources:
          limits:
            nvidia.com/gpu: 1
            memory: "16Gi"
          requests:
            memory: "8Gi"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ai-inference-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-inference-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 3. Inference Optimization

| Technique | What It Does | Speedup | Trade-off |
|-----------|-------------|---------|-----------|
| Quantization (INT8/INT4) | Reduce model weight precision | 2–4× | Slight accuracy loss |
| KV-Cache | Cache key/value attention pairs | 1.5–3× | Higher memory usage |
| Continuous Batching | Group incoming requests dynamically | 2–8× | Slightly higher latency per request |
| Speculative Decoding | Use a small model to draft tokens | 2–3× | Additional model overhead |
| PagedAttention | Efficient memory management for KV cache | 2–4× | Implementation complexity |
| Tensor Parallelism | Split model across multiple GPUs | Near-linear scaling | Requires multiple GPUs |
| Prompt Caching | Cache repeated prompt prefixes | 1.5–10× | Storage overhead |

**Quantization Example with bitsandbytes:**

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct",
    quantization_config=quantization_config,
    device_map="auto",
)
```

### 4. vLLM & LLM Serving at Scale

vLLM is the industry-standard engine for high-throughput LLM serving using PagedAttention.

**Starting a vLLM Server:**

```bash
# Install vLLM
pip install vllm

# Start OpenAI-compatible server
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --tensor-parallel-size 2 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9 \
    --port 8000
```

**Querying a vLLM Server (OpenAI-Compatible):**

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Explain PagedAttention."}],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

| Serving Engine | Best For | Key Feature |
|----------------|----------|-------------|
| vLLM | High-throughput LLM serving | PagedAttention, continuous batching |
| TGI (HuggingFace) | HuggingFace model deployment | Tight HF integration |
| NVIDIA Triton | Multi-framework GPU serving | Model ensembles, dynamic batching |
| Ollama | Local/dev LLM serving | Simple CLI, model management |
| llama.cpp | CPU and edge inference | Low-resource environments |

### 5. Serverless AI Deployment

Serverless platforms eliminate infrastructure management for AI workloads:

**Modal — Serverless GPU Functions:**

```python
import modal

app = modal.App("ai-inference")

@app.function(
    gpu="A10G",
    image=modal.Image.debian_slim().pip_install("transformers", "torch", "accelerate"),
    timeout=300,
)
def generate(prompt: str) -> str:
    from transformers import pipeline
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B-Instruct",
                    device_map="auto")
    result = pipe(prompt, max_new_tokens=256)
    return result[0]["generated_text"]

@app.local_entrypoint()
def main():
    print(generate.remote("Explain quantum computing in simple terms."))
```

**AWS Lambda for Lightweight AI:**

```python
import json
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [{"role": "user", "content": body["prompt"]}],
            "max_tokens": 512,
        }),
    )
    result = json.loads(response["body"].read())
    return {
        "statusCode": 200,
        "body": json.dumps({"response": result["content"][0]["text"]}),
    }
```

| Platform | GPU Support | Cold Start | Best For |
|----------|-------------|------------|---------|
| Modal | ✅ (A10G, A100, H100) | ~10–30s | GPU-heavy AI workloads |
| AWS Lambda | ❌ | ~1–5s | Lightweight inference, API calls |
| Google Cloud Functions | ❌ | ~1–5s | Event-driven AI pipelines |
| Google Cloud Run | ✅ (GPU preview) | ~5–30s | Containerized AI services |
| AWS SageMaker Serverless | ❌ | ~30–60s | Managed ML model hosting |
| Replicate | ✅ | ~5–15s | Open-source model hosting |
| RunPod | ✅ | ~10–30s | Custom GPU workloads |

### 6. Edge Deployment

Deploy AI models directly to edge devices for low-latency, offline-capable inference:

| Framework | Target Devices | Model Format |
|-----------|---------------|-------------|
| ONNX Runtime | CPU, GPU, mobile | .onnx |
| TensorFlow Lite | Mobile, IoT | .tflite |
| Core ML | Apple devices | .mlmodel |
| llama.cpp / GGUF | CPU, Mac, embedded | .gguf |
| NVIDIA TensorRT | NVIDIA GPUs | Optimized engine |
| Apache TVM | Cross-platform | Compiled model |

**ONNX Export and Inference:**

```python
# Export a model to ONNX
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification

model = ORTModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english", export=True
)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

inputs = tokenizer("This is a great product!", return_tensors="np")
outputs = model(**inputs)
print(outputs.logits)
```

### 7. AI Observability & Monitoring

Production AI systems require specialized observability beyond traditional APM:

```
User Request → AI Service → LLM Call → Response
     │              │            │          │
     ▼              ▼            ▼          ▼
  Request Log   Latency P99  Token Usage  Quality Score
                 Error Rate   Cost/req     User Feedback
                 Throughput   Cache Hit%   Hallucination Rate
```

| Tool | Focus Area | Key Features |
|------|-----------|-------------|
| Langfuse | LLM tracing & evaluation | Open-source, traces, scores, prompt management |
| Langsmith | LangChain observability | Deep LangChain integration, datasets, testing |
| Arize AI | ML/LLM monitoring | Drift detection, embeddings analysis, dashboards |
| Evidently AI | Data & model monitoring | Open-source, data quality, drift reports |
| Helicone | LLM proxy & analytics | Request logging, cost tracking, caching |
| Phoenix (Arize) | Local LLM tracing | Open-source, spans, evaluations |

**Langfuse Integration Example:**

```python
from langfuse.openai import openai

# Drop-in replacement — all calls are automatically traced
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is AI observability?"}],
    metadata={"user_id": "user_123", "session_id": "sess_abc"},
)
```

**Key Metrics to Track:**

| Metric | Why It Matters | Target |
|--------|---------------|--------|
| Latency (P50, P95, P99) | User experience | P95 < 2s |
| Token usage per request | Cost control | Minimize |
| Error rate | Reliability | < 0.1% |
| Cache hit rate | Cost + speed | > 30% |
| Hallucination rate | Quality | Minimize |
| User feedback score | Product quality | > 4.0/5 |
| Cost per request | Unit economics | Track trend |

### 8. AI Evaluation Systems & Pipelines

Evaluation is critical for deploying reliable AI systems:

**Evaluation Approaches:**

| Method | Description | When to Use |
|--------|-------------|-------------|
| Human Evaluation | Manual review by domain experts | Gold standard, expensive |
| LLM-as-Judge | Use GPT-4o / Claude to score outputs | Scalable, cost-effective |
| Reference-based | Compare against ground truth (BLEU, ROUGE) | When gold labels exist |
| Retrieval metrics | Precision@K, Recall@K, MRR for RAG | RAG pipeline evaluation |
| A/B testing | Compare variants with live traffic | Production validation |
| Red teaming | Adversarial testing for safety | Pre-deployment |

**LLM-as-Judge Example:**

```python
from openai import OpenAI

client = OpenAI()

def evaluate_response(question: str, response: str) -> dict:
    eval_prompt = f"""Rate the following AI response on a scale of 1-5 for:
    1. Relevance: Does it answer the question?
    2. Accuracy: Is the information correct?
    3. Completeness: Does it cover all key points?

    Question: {question}
    Response: {response}

    Return JSON: {{"relevance": X, "accuracy": X, "completeness": X, "reasoning": "..."}}"""

    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": eval_prompt}],
        response_format={"type": "json_object"},
    )
    return result.choices[0].message.content
```

### 9. AI System Design Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Gateway Pattern | Central API gateway routes to AI services | Multi-model routing |
| Sidecar Pattern | Monitoring/logging alongside AI service | Observability |
| Circuit Breaker | Fallback when AI service is down | High availability |
| Semantic Cache | Cache based on meaning, not exact match | Reduce redundant LLM calls |
| Retrieval-Augmented Generation | Combine retrieval with generation | Grounded AI responses |
| Guardrail Pipeline | Input/output validation around LLM | Safety and compliance |
| Fan-out / Fan-in | Parallel LLM calls, aggregate results | Complex analysis tasks |
| Model Router | Route to different models by task complexity | Cost optimization |

**Model Router Pattern:**

```python
from openai import OpenAI

client = OpenAI()

def classify_complexity(query: str) -> str:
    """Route queries to appropriate models based on complexity."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify as 'simple' or 'complex'."},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content.strip().lower()

def route_query(query: str) -> str:
    complexity = classify_complexity(query)
    model = "gpt-4o-mini" if complexity == "simple" else "gpt-4o"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
    )
    return response.choices[0].message.content
```

### 10. AI Security & Safety

| Threat | Description | Mitigation |
|--------|-------------|------------|
| Prompt Injection | Malicious input overrides system prompt | Input validation, guardrails |
| Jailbreaking | Bypass model safety filters | Multi-layer defense, output filtering |
| Data Exfiltration | Extract training data or system prompts | Minimize sensitive data in prompts |
| PII Leakage | Model exposes personal information | PII detection/redaction (Presidio) |
| Hallucination | Confidently generates false information | RAG, citations, confidence scoring |
| Denial of Wallet | Excessive API calls drain budget | Rate limiting, cost caps |

**Guardrails Implementation:**

```python
from guardrails import Guard
from guardrails.hub import ToxicLanguage, DetectPII

guard = Guard().use_many(
    ToxicLanguage(on_fail="exception"),
    DetectPII(pii_entities=["EMAIL_ADDRESS", "PHONE_NUMBER"], on_fail="fix"),
)

result = guard(
    llm_api=openai.chat.completions.create,
    model="gpt-4o",
    messages=[{"role": "user", "content": user_input}],
)
```

**Key Security Practices:**
- Never expose API keys in client-side code
- Implement rate limiting per user and per IP
- Add input length limits and content filtering
- Log and monitor all AI interactions
- Use separate API keys for development and production
- Implement cost caps and usage alerts
- Regularly audit model outputs for bias and safety

### 11. Cost Optimization for AI Systems

| Strategy | Implementation | Savings |
|----------|---------------|---------|
| Model routing | Use cheaper models for simple tasks | 40–70% |
| Semantic caching | Cache similar queries with embeddings | 20–50% |
| Prompt optimization | Shorter, more efficient prompts | 10–30% |
| Batch processing | Group non-urgent requests | 30–50% |
| Spot/preemptible instances | Use discounted cloud GPUs | 60–80% |
| Quantized models | Use INT4/INT8 for self-hosted models | 50–75% (compute) |
| Output token limits | Cap `max_tokens` per request | 10–40% |

**Cost Tracking Example:**

```python
import tiktoken

def estimate_cost(model: str, messages: list, max_tokens: int = 500) -> float:
    """Estimate the cost of an API call before making it."""
    pricing = {
        "gpt-4o":      {"input": 2.50 / 1_000_000, "output": 10.00 / 1_000_000},
        "gpt-4o-mini": {"input": 0.15 / 1_000_000, "output": 0.60 / 1_000_000},
    }
    enc = tiktoken.encoding_for_model(model)
    input_tokens = sum(len(enc.encode(m["content"])) for m in messages)
    input_cost = input_tokens * pricing[model]["input"]
    output_cost = max_tokens * pricing[model]["output"]
    return input_cost + output_cost
```

### 12. API Gateway & Rate Limiting

```python
from fastapi import FastAPI, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

@app.post("/api/chat")
@limiter.limit("10/minute")
async def chat(request):
    """Rate-limited AI chat endpoint."""
    # Validate input
    if len(request.message) > 4000:
        raise HTTPException(status_code=400, detail="Message too long")

    response = await call_llm(request.message)
    return {"response": response}
```

### 13. Model Versioning & A/B Testing

**A/B Testing Framework for AI:**

```python
import random
import hashlib

def get_model_variant(user_id: str, experiment: str = "model_v2_test") -> str:
    """Deterministic A/B assignment based on user ID."""
    hash_input = f"{user_id}:{experiment}"
    hash_value = int(hashlib.sha256(hash_input.encode()).hexdigest(), 16)
    bucket = hash_value % 100

    if bucket < 50:
        return "gpt-4o-mini"       # Control (50%)
    else:
        return "gpt-4o"            # Treatment (50%)

def log_experiment(user_id: str, variant: str, latency: float, quality_score: float):
    """Log A/B test metrics for analysis."""
    metrics = {
        "user_id": user_id,
        "variant": variant,
        "latency_ms": latency,
        "quality_score": quality_score,
        "timestamp": datetime.utcnow().isoformat(),
    }
    # Send to your analytics pipeline (PostHog, Langfuse, etc.)
    analytics.track(metrics)
```

| Versioning Strategy | Tool | Description |
|---------------------|------|-------------|
| Model Registry | MLflow, W&B | Version and stage models |
| Prompt Versioning | Langfuse, PromptLayer | Track prompt iterations |
| Feature Flags | LaunchDarkly, PostHog | Gradual rollout of new models |
| Shadow Mode | Custom | Run new model alongside old, compare |
| Canary Deployment | Kubernetes | Route small % of traffic to new version |

### 14. AI Product Engineering

Building AI-powered products requires combining AI capabilities with solid product engineering:

**The AI Product Stack:**

```
User Interface (Next.js / Streamlit / React)
       ↓
Authentication (Clerk / Supabase Auth / Auth.js)
       ↓
API Layer (FastAPI / Next.js API Routes)
       ↓
AI Services (LLM APIs / vLLM / RAG Pipeline)
       ↓
Data Layer (PostgreSQL / Redis / Vector DB)
       ↓
Payments (Stripe)
       ↓
Infrastructure (Docker / Kubernetes / Cloud)
       ↓
Monitoring (Langfuse / PostHog / Sentry)
```

**SaaS Monetization Models for AI Products:**

| Model | Description | Example |
|-------|-------------|---------|
| Freemium | Free basic tier, paid premium | Notion AI |
| Usage-based | Pay per API call or token | OpenAI API |
| Subscription | Monthly/yearly flat fee | GitHub Copilot |
| Per-seat | Pay per team member | Jasper AI |
| Enterprise | Custom pricing, dedicated infra | Large RAG deployments |

**Key Product Principles:**
1. **Start with the problem** — AI should solve a real pain point, not be a gimmick
2. **Validate before building** — Talk to 10 potential users first
3. **Ship fast, iterate faster** — Launch an MVP in 2 weeks
4. **Measure what matters** — Track retention, not just signups
5. **Manage AI costs** — Know your cost per request from day one

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Docker | Containerization |
| Kubernetes | Container orchestration |
| vLLM | High-throughput LLM serving |
| NVIDIA Triton | GPU inference server |
| Modal | Serverless GPU functions |
| AWS (EC2, Lambda, SageMaker) | Cloud compute and ML services |
| GCP (Cloud Run, Vertex AI) | Cloud compute and ML services |
| FastAPI | API development |
| Langfuse | LLM observability (open-source) |
| Langsmith | LangChain tracing and evaluation |
| Arize AI | ML/LLM monitoring |
| Evidently AI | Data and model monitoring |
| ONNX Runtime | Cross-platform inference |
| Guardrails AI | LLM output validation |
| Stripe | Payment integration |
| PostHog | Product analytics |
| Redis | Caching layer |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| vLLM Documentation | Official | https://docs.vllm.ai/ |
| Docker Documentation | Official | https://docs.docker.com/ |
| Kubernetes Documentation | Official | https://kubernetes.io/docs/ |
| Langfuse Documentation | Official | https://langfuse.com/docs |
| Full Stack Deep Learning | Free Course | https://fullstackdeeplearning.com/ |
| Made With ML — MLOps | Free Course | https://madewithml.com/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_docker_gpu_serving.md` — Containerize an LLM service with GPU support
- `02_vllm_deployment.ipynb` — Deploy and benchmark a model with vLLM
- `03_inference_optimization.ipynb` — Compare quantized vs. full-precision inference
- `04_langfuse_tracing.ipynb` — Add observability to an LLM application
- `05_serverless_deployment.md` — Deploy an AI function on Modal
- `06_ab_testing.ipynb` — Implement A/B testing for model variants
- `07_security_guardrails.ipynb` — Add input/output guardrails to an AI endpoint

---

## 🛠️ Mini Projects

1. **LLM Inference Server** — Deploy a quantized open-source LLM with vLLM behind a FastAPI gateway with rate limiting and health checks
2. **AI Observability Dashboard** — Instrument an LLM app with Langfuse tracing, build a cost and quality monitoring dashboard
3. **Serverless AI Pipeline** — Build an event-driven document processing pipeline using Modal with GPU-accelerated inference
4. **AI Security Audit** — Test an AI endpoint for prompt injection, implement guardrails, and document the security posture

---

## 🏆 Major Projects

### Project 1: Real-Time AI Chatbot with Streaming, Monitoring & Auto-Scaling

Build a production-grade AI chatbot that handles real-time conversations at scale.

**Description:**
Deploy an LLM-powered chatbot with server-sent events (SSE) streaming, comprehensive observability, and Kubernetes-based auto-scaling. The system should handle hundreds of concurrent users while maintaining low latency and high quality.

**Technologies:**
- **Serving:** vLLM or TGI for LLM inference
- **API:** FastAPI with WebSocket/SSE streaming
- **Infrastructure:** Docker, Kubernetes with HPA (Horizontal Pod Autoscaler)
- **Monitoring:** Langfuse for tracing, Prometheus + Grafana for metrics
- **Cache:** Redis for semantic caching of frequent queries
- **Security:** Rate limiting, input validation, guardrails

**Expected Learning Outcomes:**
- Configure and optimize vLLM for production throughput
- Implement real-time streaming responses with Server-Sent Events
- Set up Kubernetes auto-scaling based on GPU utilization and request queue depth
- Build a full observability stack with traces, metrics, and alerts
- Implement semantic caching to reduce costs and latency
- Handle failure modes: timeouts, retries, circuit breakers

See [projects/](./projects/) for the full template.

---

### Project 2: AI SaaS Product — End-to-End with Auth, Payments & Deployment

Build and launch a complete AI-powered SaaS product with real users.

**Description:**
Design, build, and deploy a monetizable AI product from scratch. This includes user authentication, subscription billing, a polished UI, LLM-powered features, and production infrastructure. The goal is to have a live product URL with at least 10 beta users.

**Technologies:**
- **Frontend:** Next.js or Streamlit
- **Backend:** FastAPI with async endpoints
- **Auth:** Clerk or Supabase Auth
- **Payments:** Stripe (subscription billing)
- **AI:** OpenAI API or self-hosted LLM via vLLM
- **Database:** PostgreSQL (Supabase or Neon) + Redis
- **Vector Store:** pgvector or Pinecone (if RAG-based)
- **Deployment:** Vercel (frontend) + Railway or Render (backend) + Modal (GPU)
- **Monitoring:** Langfuse + PostHog + Sentry

**Expected Learning Outcomes:**
- Architect a full-stack AI product from database to deployment
- Integrate payment processing with usage-based or subscription billing
- Implement secure user authentication and authorization
- Manage AI costs with caching, model routing, and token budgets
- Deploy and maintain a production system with CI/CD
- Collect user feedback and iterate on the product
- Understand unit economics: cost per user, LTV, CAC

See [projects/](./projects/) for the full template.

---

## ✅ Stage Completion Checklist

- [ ] Deployed an AI model to a cloud platform (AWS, GCP, or Azure)
- [ ] Containerized an AI service with Docker and run it with GPU support
- [ ] Served an LLM with vLLM and benchmarked throughput
- [ ] Deployed a serverless AI function on Modal or AWS Lambda
- [ ] Implemented inference optimization (quantization or caching)
- [ ] Added observability to an LLM app with Langfuse or Langsmith
- [ ] Built an evaluation pipeline (LLM-as-Judge or reference-based)
- [ ] Implemented security guardrails (prompt injection defense, PII filtering)
- [ ] Set up API rate limiting and cost tracking
- [ ] Built and deployed a streaming AI chatbot with auto-scaling
- [ ] Shipped an AI SaaS product with auth, payments, and monitoring
- [ ] Pushed all projects to GitHub with documentation

**Next Stage → [09 AI Projects](../09-ai-projects/)**
