# Stage 9 — Real-World AI Projects

## 🎯 Overview

This stage contains **20 complete, real-world AI projects** ranging from beginner to advanced. Each project includes a description, technologies used, and expected learning outcomes so you know exactly what you will build and what skills you will gain.

**Choose projects that align with your target role or startup idea.**

---

## 📊 Project Index

| # | Project | Difficulty | Key Tech | Time |
|---|---------|-----------|---------|------|
| 01 | [Resume Screening AI](#project-1-resume-screening-ai) | ⭐⭐ | NLP, Scikit-learn | 3 days |
| 02 | [ChatGPT-like Chatbot](#project-2-chatgpt-like-chatbot) | ⭐⭐ | LangChain, Streamlit | 2 days |
| 03 | [AI Code Assistant](#project-3-ai-code-assistant) | ⭐⭐⭐ | CodeLLM, VSCode ext | 5 days |
| 04 | [AI Document Search (RAG)](#project-4-ai-document-search-rag) | ⭐⭐⭐ | RAG, Vector DB | 4 days |
| 05 | [AI Image Classifier](#project-5-ai-image-classifier) | ⭐⭐ | CNN, PyTorch | 4 days |
| 06 | [Fraud Detection System](#project-6-fraud-detection-system) | ⭐⭐⭐ | XGBoost, Imbalanced-learn | 5 days |
| 07 | [AI Recommendation System](#project-7-ai-recommendation-system) | ⭐⭐⭐ | Collaborative filtering | 5 days |
| 08 | [AI Customer Support Bot](#project-8-ai-customer-support-bot) | ⭐⭐⭐ | Agents, LangChain | 5 days |
| 09 | [Multi-Agent AI System](#project-9-multi-agent-ai-system) | ⭐⭐⭐⭐ | LangGraph, Agents | 7 days |
| 10 | [Sentiment Analysis Dashboard](#project-10-sentiment-analysis-dashboard) | ⭐⭐ | BERT, Streamlit | 3 days |
| 11 | [Stock Price Predictor](#project-11-stock-price-predictor) | ⭐⭐⭐ | LSTM, time series | 4 days |
| 12 | [Multimodal AI Application](#project-12-multimodal-ai-application) | ⭐⭐⭐⭐ | GPT-4V, CLIP, Whisper | 7 days |
| 13 | [AI Research Paper Summarizer](#additional-projects) | ⭐⭐ | RAG, PDF parsing | 3 days |
| 14 | [AI Meeting Summarizer](#additional-projects) | ⭐⭐ | Whisper, LLM | 3 days |
| 15 | [Fake News Detector](#additional-projects) | ⭐⭐ | NLP, ML | 3 days |
| 16 | [AI-Powered Job Board](#additional-projects) | ⭐⭐⭐ | RAG, FastAPI | 5 days |
| 17 | [AI Email Generator](#additional-projects) | ⭐⭐ | Prompt engineering | 2 days |
| 18 | [Medical Diagnosis Assistant](#additional-projects) | ⭐⭐⭐ | ML, explainability | 5 days |
| 19 | [AI Content Moderator](#additional-projects) | ⭐⭐ | Zero-shot LLM | 2 days |
| 20 | [Personalized AI Learning Tutor](#additional-projects) | ⭐⭐⭐⭐ | Agents, memory | 7 days |

---

## Project Details

### Project 1: Resume Screening AI

**Description:** Build an intelligent resume screening tool that automatically parses, ranks, and filters candidate resumes against a given job description using semantic similarity and NLP techniques.

**Technologies:** Python, Scikit-learn, HuggingFace sentence-transformers, Streamlit, PDF/DOCX parsing libraries

**Learning Outcomes:**
- Apply NLP techniques (TF-IDF, sentence embeddings) to real-world text matching problems
- Build end-to-end ML pipelines that ingest unstructured documents and produce ranked outputs
- Design user-facing AI tools with explainable scoring for non-technical stakeholders

---

### Project 2: ChatGPT-like Chatbot

**Description:** Create a conversational chatbot with multi-turn memory and real-time streaming responses, supporting multiple LLM backends and system prompt customization.

**Technologies:** LangChain, OpenAI API / Ollama, Streamlit, Python

**Learning Outcomes:**
- Implement conversation memory management and multi-turn dialogue handling
- Build streaming response interfaces that deliver token-by-token output to the user
- Configure and swap between different LLM providers using a unified framework

---

### Project 3: AI Code Assistant

**Description:** Develop a coding assistant that can explain code, generate functions from natural language descriptions, fix bugs with detailed explanations, and automatically write unit tests and docstrings.

**Technologies:** CodeLlama / GPT-4, FastAPI, VS Code Extension API, Python

**Learning Outcomes:**
- Work with code-specialized LLMs and craft effective prompts for code generation tasks
- Build a VS Code extension that integrates AI capabilities into a developer workflow
- Design multi-task AI systems that handle explanation, generation, and debugging in a unified interface

---

### Project 4: AI Document Search (RAG)

**Description:** Build a production-grade Retrieval-Augmented Generation system that indexes thousands of enterprise documents and answers user queries with source citations using hybrid semantic and keyword search.

**Technologies:** LangChain, Pinecone / Chroma, FastAPI, React or Streamlit, sentence-transformers

**Learning Outcomes:**
- Architect and deploy a full RAG pipeline including document ingestion, chunking, embedding, and retrieval
- Implement hybrid search combining dense vector similarity with sparse keyword matching
- Build production-ready AI systems with admin panels, usage analytics, and scalable vector storage

---

### Project 5: AI Image Classifier

**Description:** Build a production-grade image classification system by fine-tuning a pretrained CNN on a custom dataset, complete with explainability visualizations (Grad-CAM), a drag-and-drop UI, and a Dockerized deployment.

**Technologies:** PyTorch, ResNet / EfficientNet, FastAPI, Streamlit, Docker, Grad-CAM

**Learning Outcomes:**
- Apply transfer learning to fine-tune pretrained models on domain-specific image datasets
- Implement Grad-CAM visualizations to explain model predictions and build trust with users
- Containerize and deploy deep learning models as production-ready API services

---

### Project 6: Fraud Detection System

**Description:** Build an end-to-end fraud detection pipeline that identifies fraudulent transactions in real time using machine learning models trained on highly imbalanced financial datasets, with explainable predictions and an alerting dashboard.

**Technologies:** Python, XGBoost, Scikit-learn, Imbalanced-learn (SMOTE), SHAP, FastAPI, Streamlit, Docker

**Learning Outcomes:**
- Handle severely imbalanced datasets using resampling techniques (SMOTE, undersampling) and appropriate evaluation metrics (precision-recall, F1, AUC-ROC)
- Build real-time inference pipelines that score incoming transactions and trigger fraud alerts
- Apply SHAP-based model explainability to surface the key features driving each fraud prediction

---

### Project 7: AI Recommendation System

**Description:** Build a product or content recommendation engine that combines collaborative filtering, content-based filtering, and a hybrid approach, with strategies for the cold-start problem and an A/B testing framework.

**Technologies:** Scikit-learn, Surprise library, Matrix Factorization (SVD), FastAPI, Python

**Learning Outcomes:**
- Implement collaborative filtering and content-based recommendation algorithms from scratch
- Design hybrid recommendation strategies and evaluate them with ranking metrics (MAP, NDCG)
- Build a real-time recommendation API with cold-start handling and an A/B testing framework

---

### Project 8: AI Customer Support Bot

**Description:** Create an intelligent customer support chatbot that answers FAQs from a knowledge base using RAG, handles multi-turn conversations, and escalates complex issues to human agents when confidence is low.

**Technologies:** LangChain Agents, RAG, Pinecone / Chroma, FastAPI, Streamlit

**Learning Outcomes:**
- Build agentic AI systems that combine retrieval, reasoning, and function calling
- Implement confidence-based escalation logic for graceful human handoff
- Design conversation analytics dashboards to monitor bot performance and identify knowledge gaps

---

### Project 9: Multi-Agent AI System

**Description:** Build a multi-agent research assistant where specialized agents (Planner, Researcher, Fact-Checker, Writer) collaborate autonomously to gather information from the web and produce verified, well-structured reports.

**Technologies:** LangGraph, OpenAI, Tavily Search API, FastAPI, Python

**Learning Outcomes:**
- Design and orchestrate multi-agent workflows with explicit state management using LangGraph
- Implement tool-using agents that autonomously search, verify, and synthesize information
- Build reliable agent pipelines with error handling, retries, and human-in-the-loop checkpoints

---

### Project 10: Sentiment Analysis Dashboard

**Description:** Build a real-time sentiment analysis dashboard that processes social media posts and product reviews, visualizes sentiment trends over time, extracts key discussion topics, and supports competitor comparison.

**Technologies:** HuggingFace BERT / Transformers, FastAPI, Streamlit, Plotly, Python

**Learning Outcomes:**
- Fine-tune and deploy transformer-based NLP models for sentiment classification
- Build real-time data pipelines that scrape, process, and visualize streaming text data
- Create interactive dashboards with trend analysis, topic extraction, and comparative analytics

---

### Project 11: Stock Price Predictor

**Description:** Predict stock price movements by combining LSTM time-series models with sentiment analysis from financial news, featuring uncertainty quantification, interactive Plotly charts, and a backtesting framework.

**Technologies:** PyTorch (LSTM), yfinance, OpenAI / LLM for sentiment, FastAPI, Streamlit, Plotly

**Learning Outcomes:**
- Build and train LSTM networks for time-series forecasting with proper train/validation/test splits
- Combine structured numerical data with unstructured text sentiment as multi-signal input features
- Implement backtesting frameworks to evaluate trading strategies and quantify prediction uncertainty

---

### Project 12: Multimodal AI Application

**Description:** Build a multimodal AI application that accepts and reasons over text, images, and audio inputs simultaneously—enabling use cases such as visual question answering, image-captioning with voice queries, and cross-modal search.

**Technologies:** GPT-4V / LLaVA, OpenAI CLIP, OpenAI Whisper, LangChain, FastAPI, Streamlit, Python

**Learning Outcomes:**
- Integrate multiple AI modalities (vision, language, audio) into a unified application pipeline
- Work with state-of-the-art multimodal models (GPT-4V, CLIP, Whisper) and understand their capabilities and limitations
- Design intuitive user interfaces that handle heterogeneous input types and present coherent cross-modal outputs

---

## Additional Projects

The following projects follow the same hands-on format. Refer to each project folder for the full specification, starter code, and deployment instructions.

| # | Project | Description | Technologies | Time |
|---|---------|-------------|-------------|------|
| 13 | AI Research Paper Summarizer | Upload research PDFs and get structured summaries, Q&A, and cross-paper comparisons | LangChain, Chroma, sentence-transformers, Streamlit | 3 days |
| 14 | AI Meeting Summarizer | Transcribe meeting recordings and extract summaries, action items, and key decisions with speaker diarization | OpenAI Whisper, GPT-4, FastAPI, Streamlit | 3 days |
| 15 | Fake News Detector | Classify news articles as real or fake with SHAP-based explainability and a credibility score | NLP, XGBoost, BERT, SHAP, FastAPI | 3 days |
| 16 | AI-Powered Job Board | Smart job board with semantic job search, resume-to-job matching, and auto-generated cover letters | FastAPI, PostgreSQL, Pinecone, React/Streamlit | 5 days |
| 17 | AI Email Generator | Generate personalized outreach emails with tone adjustment and A/B test variations | OpenAI/LLM, FastAPI, Streamlit | 2 days |
| 18 | Medical Diagnosis Assistant | Assist doctors with preliminary diagnosis from symptoms using ML with SHAP explainability | Scikit-learn, SHAP, FastAPI, Streamlit | 5 days |
| 19 | AI Content Moderator | Detect harmful, toxic, or policy-violating content using zero-shot classification | HuggingFace zero-shot, FastAPI, Streamlit | 2 days |
| 20 | Personalized AI Learning Tutor | Adaptive AI tutor that adjusts difficulty, tracks progress, and generates personalized study plans | LangChain, LangGraph, vector memory, Streamlit | 7 days |

---

## 🚀 Getting Started with Any Project

```bash
# 1. Navigate to the project folder
cd projects/01-resume-screening-ai/

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# 4. Run the project
streamlit run app.py
# or
uvicorn api:app --reload
```

---

## 🏆 Project Showcase

After completing projects, share them here by opening a PR!

| Student | Project | Demo Link | GitHub |
|---------|---------|-----------|--------|
| — | — | — | — |

**Next Stage → [10 Career Prep](../10-career-prep/)**
