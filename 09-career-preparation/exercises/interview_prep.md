# AI Engineer Interview Preparation Guide

A comprehensive set of interview questions and answers for AI/ML engineering roles.

---

## 📋 Machine Learning Fundamentals

### Q1: What is the bias-variance tradeoff?

**Answer:**
- **Bias** = error from wrong assumptions in the model (underfitting)
- **Variance** = error from sensitivity to small fluctuations in training data (overfitting)
- **Total Error = Bias² + Variance + Irreducible Noise**
- Simple models (linear) → high bias, low variance
- Complex models (deep nets) → low bias, high variance
- **Solution:** Find the sweet spot via regularization, cross-validation, and ensemble methods

---

### Q2: What's the difference between L1 and L2 regularization?

| | L1 (Lasso) | L2 (Ridge) |
|---|---|---|
| **Penalty** | Sum of absolute weights | Sum of squared weights |
| **Effect** | Sparsity (drives weights to 0) | Shrinks all weights |
| **Use when** | Feature selection, many irrelevant features | All features are relevant |
| **Solution** | Non-differentiable at 0 | Always differentiable |

---

### Q3: How does gradient descent work?

1. Initialize weights randomly
2. Compute the loss (e.g., MSE, cross-entropy)
3. Compute gradient: ∂Loss/∂weights
4. Update: weights = weights - learning_rate × gradient
5. Repeat until convergence

**Variants:**
- **Batch GD** — Uses all training data per step (slow, stable)
- **SGD** — Uses 1 sample per step (fast, noisy)
- **Mini-batch GD** — Uses N samples per step (best of both)

---

### Q4: Explain attention mechanism in transformers

The attention mechanism lets a model focus on different parts of the input for each output token.

**Scaled dot-product attention:**
```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) × V
```

- **Q (Query)** — What we're looking for
- **K (Key)** — What each position offers
- **V (Value)** — The actual content

**Self-attention** = Q, K, V all come from the same sequence.

---

### Q5: What is RAG and when would you use it?

**RAG (Retrieval-Augmented Generation):**
1. Embed documents in a vector database
2. Embed user query
3. Retrieve top-K most similar documents
4. Pass retrieved docs + query to LLM
5. LLM generates answer grounded in retrieved context

**Use RAG when:**
- Knowledge needs to be up-to-date (LLMs have training cutoffs)
- Need to cite sources
- Domain-specific knowledge not in training data
- Context window would be too large for all docs

---

## 🏗️ System Design Questions

### Design a Real-Time Fraud Detection System

**Components:**
1. **Data ingestion** — Kafka stream of transactions
2. **Feature engineering** — Real-time feature computation (velocity, patterns)
3. **Model serving** — Low-latency ML model (<50ms)
4. **Decision engine** — Threshold-based approve/flag/deny
5. **Feedback loop** — Manual reviews update training data
6. **Retraining pipeline** — Weekly model updates

**Key challenges:**
- Extreme class imbalance (fraud is rare)
- Must be real-time (< 100ms)
- False positives frustrate customers

---

### Design a Document Search System (RAG at Scale)

**For 10 million documents:**

1. **Ingestion pipeline** — Parse PDFs, chunk documents (512 tokens), generate embeddings
2. **Vector DB** — Pinecone with 1536-dim vectors, approximate nearest neighbor (ANN)
3. **Metadata filtering** — Filter by department, date, category before vector search
4. **Hybrid search** — Combine BM25 (keyword) + semantic search
5. **Answer generation** — GPT-4 with retrieved context
6. **Caching** — Cache popular queries with Redis
7. **Scaling** — Horizontal scaling, read replicas

---

## 💻 Coding Questions

### Implement K-Means Clustering

```python
import numpy as np

def kmeans(X, k, max_iters=100, random_state=42):
    np.random.seed(random_state)
    
    # Initialize centroids randomly
    idx = np.random.choice(len(X), k, replace=False)
    centroids = X[idx]
    
    for _ in range(max_iters):
        # Assign clusters
        distances = np.linalg.norm(X[:, None] - centroids[None, :], axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        # Check convergence
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids
```

### Implement Softmax

```python
def softmax(x):
    # Subtract max for numerical stability
    x = x - x.max(axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / exp_x.sum(axis=-1, keepdims=True)
```

---

## 🤖 LLM-Specific Questions

**Q: What is the difference between BERT and GPT?**

| | BERT | GPT |
|---|---|---|
| **Architecture** | Encoder only | Decoder only |
| **Training** | Masked language modeling | Next token prediction |
| **Direction** | Bidirectional | Unidirectional (left to right) |
| **Best for** | Classification, QA, NER | Text generation, chat |

**Q: How do you evaluate a RAG system?**
- **Retrieval metrics:** Hit Rate, MRR (Mean Reciprocal Rank), NDCG
- **Generation metrics:** Faithfulness, Answer Relevancy, Context Relevancy
- **Tools:** RAGAS library, LangSmith

**Q: What is LLM hallucination and how do you reduce it?**
- Hallucination = LLM generates confident but false information
- Reduce with: RAG (ground in facts), lower temperature, structured outputs, fact-checking agents
