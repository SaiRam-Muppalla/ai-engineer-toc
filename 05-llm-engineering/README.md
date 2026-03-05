# Stage 5 — LLM Engineering

## 🎯 Learning Objectives

By the end of this stage you will:
- Master prompt engineering for production use cases
- Build RAG (Retrieval-Augmented Generation) systems from scratch
- Work with vector databases (FAISS, Pinecone, Weaviate)
- Fine-tune open-source LLMs with LoRA/QLoRA
- Understand foundations of AI agents and tool use

## ⏱️ Estimated Time: 3 weeks

---

## 📐 Key Concepts

### 1. Prompt Engineering

| Technique | Description |
|-----------|-------------|
| Zero-shot prompting | Ask the model without examples |
| Few-shot prompting | Provide 2–5 examples in the prompt |
| Chain-of-thought (CoT) | Ask model to reason step by step |
| ReAct prompting | Reasoning + Acting in interleaved steps |
| System prompts | Control model persona and behavior |
| Prompt chaining | Connect multiple prompts in a pipeline |
| Prompt templates | Reusable, parameterized prompts |

### 2. RAG Systems (Retrieval-Augmented Generation)

```
Documents → Chunk → Embed → Store in Vector DB
                                    ↓
User Query → Embed → Search Vector DB → Top-K Chunks + LLM → Answer
```

**Components:**
- Document loaders (PDF, web, CSV, code)
- Text splitters (recursive, semantic)
- Embedding models (OpenAI, HuggingFace, Cohere)
- Vector databases (FAISS, Pinecone, Weaviate, Chroma)
- Retrieval strategies (similarity search, MMR, hybrid)
- Answer generation with context

### 3. Vector Databases

| Database | Type | Best For |
|----------|------|---------|
| FAISS | Local library | Prototyping, small scale |
| Chroma | Local/cloud | Development, open source |
| Pinecone | Managed cloud | Production, serverless |
| Weaviate | Self-hosted/cloud | Enterprise, multimodal |
| Qdrant | Self-hosted/cloud | High performance |

### 4. Fine-Tuning LLMs

| Method | Description | VRAM Required |
|--------|-------------|--------------|
| Full fine-tuning | Update all parameters | 80GB+ |
| LoRA | Low-rank adapters | 16–24GB |
| QLoRA | Quantized LoRA | 8–12GB |
| Prompt tuning | Only tune prompt tokens | 4–8GB |
| RLHF / DPO | Alignment fine-tuning | 16GB+ |

**Tools:** HuggingFace PEFT, TRL, bitsandbytes, Axolotl

### 5. AI Agents (Overview)

- **Tool use:** Give LLMs access to functions (web search, calculator, APIs)
- **ReAct agents:** Reason → Act → Observe → Repeat
- **Memory:** Short-term (context window), long-term (vector DB)

**For in-depth coverage of AI agents, see [Stage 6 — AI Agents](../06-ai-agents/)**

### 6. LLM Frameworks

| Framework | Use Case |
|-----------|---------|
| LangChain | General-purpose LLM apps |
| LlamaIndex | Document indexing and RAG |

> Agent-specific frameworks (LangGraph, CrewAI, AutoGen) are covered in [Stage 6 — AI Agents](../06-ai-agents/).

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| OpenAI API | GPT-4, embeddings, vision |
| HuggingFace Hub | Open-source LLMs |
| LangChain | LLM application framework |
| LlamaIndex | RAG and document indexing |
| FAISS | Local vector search |
| Pinecone | Managed vector DB |
| Chroma | Open-source vector DB |
| HuggingFace PEFT | LoRA/QLoRA fine-tuning |
| Ollama | Run LLMs locally |
| Replicate | GPU inference API |
| Groq | Ultra-fast LLM inference |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| LangChain Docs | Official Docs | https://python.langchain.com/docs/ |
| LlamaIndex Docs | Official Docs | https://docs.llamaindex.ai/ |
| Prompt Engineering Guide | Free Guide | https://www.promptingguide.ai/ |
| HuggingFace NLP Course | Free Course | https://huggingface.co/learn/nlp-course |
| RAG from scratch (LangChain) | YouTube | https://www.youtube.com/watch?v=wd7TZ4w1mSw |
| LLM Agents (DeepLearning.AI) | Free Course | https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_prompt_engineering.ipynb` — Master all major prompting techniques
- `02_langchain_basics.ipynb` — Build your first LangChain pipeline
- `03_rag_from_scratch.ipynb` — Build RAG with FAISS without using any framework
- `04_vector_databases.ipynb` — Compare FAISS, Chroma, and Pinecone
- `05_ai_agents.ipynb` — Build a tool-using ReAct agent

---

## 🛠️ Mini Projects

1. **Prompt Engineering Playbook** — A Jupyter notebook with 15+ prompting techniques demonstrated
2. **Personal Wikipedia Bot** — RAG over Wikipedia articles for a specific topic
3. **Code Review Bot** — An agent that reviews Python code and suggests improvements

---

## 🏆 Major Projects

### Project 1: AI Research Paper Summarizer (RAG)

Build a system that lets users upload PDF research papers and ask questions.

**Features:**
- Upload multiple PDFs
- Chunk and embed using sentence-transformers
- Store in Chroma vector database
- Semantic search with MMR (diversity)
- Cite sources in every answer
- Compare papers side by side
- Streamlit UI with file upload

See [projects/](./projects/) for full project templates.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 5 exercises
- [ ] Built the personal Wikipedia bot
- [ ] Built the code review bot
- [ ] Completed the RAG paper summarizer
- [ ] Pushed everything to GitHub

> For agent-related projects, see [Stage 6 — AI Agents](../06-ai-agents/).

**Next Stage → [06 AI Agents](../06-ai-agents/)**
