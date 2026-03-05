# Project 1: AI Research Paper Summarizer (RAG System)

Ask questions about uploaded research papers using a RAG pipeline.

## 📋 Features

- Upload multiple PDF research papers
- Semantic search across all papers
- Cite source paragraphs in every answer
- Compare two papers side by side
- Export Q&A session as a report

## 🏗️ Architecture

```
PDF Upload → Text Extraction → Chunking → Embedding (sentence-transformers)
                                                      ↓
                                            Chroma Vector DB
                                                      ↓
User Query → Embed Query → Semantic Search → Top-K Chunks → GPT-4 → Answer + Sources
```

## 🚀 Getting Started

```bash
pip install langchain langchain-openai chromadb sentence-transformers pypdf streamlit

# Set your OpenAI API key
export OPENAI_API_KEY='your-key'

# Run the app
streamlit run app.py
```

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit UI with PDF upload |
| `rag_pipeline.py` | Core RAG logic |
| `chunker.py` | Document chunking strategies |
| `embedder.py` | Embedding utilities |
| `requirements.txt` | Dependencies |

## 💡 Key Learning Points

1. **Chunking strategy matters** — Try different chunk sizes (256, 512, 1024 tokens)
2. **Embedding model choice** — Compare `all-MiniLM-L6-v2` vs `text-embedding-3-small`
3. **Retrieval quality** — Evaluate with Hit Rate and MRR metrics
4. **Context window management** — Handle long contexts with summarization
