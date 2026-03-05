# Tutorial: Setting Up Your AI Development Environment

This guide will get your machine ready for all stages of the curriculum.

## 🐍 1. Install Python 3.10+

**Windows:**
```bash
# Download from python.org or use winget
winget install Python.Python.3.10
```

**macOS:**
```bash
brew install python@3.10
```

**Linux:**
```bash
sudo apt update && sudo apt install python3.10 python3.10-venv python3-pip
```

---

## 📦 2. Create a Virtual Environment

Always use a virtual environment for each project!

```bash
# Create virtual environment
python -m venv ai-env

# Activate it
# Windows:
ai-env\Scripts\activate
# macOS/Linux:
source ai-env/bin/activate
```

---

## 🔧 3. Install Core AI Libraries

```bash
# Foundations
pip install numpy pandas matplotlib seaborn

# Machine Learning
pip install scikit-learn xgboost lightgbm

# Deep Learning
pip install torch torchvision torchaudio  # CPU
# For GPU: visit pytorch.org for the right command

# Transformers
pip install transformers datasets tokenizers accelerate

# LLM Engineering
pip install langchain langchain-openai langchain-community
pip install llama-index chromadb faiss-cpu sentence-transformers

# MLOps
pip install fastapi uvicorn[standard] mlflow streamlit

# Utilities
pip install jupyter notebook python-dotenv requests tqdm
```

---

## 🔑 4. Set Up API Keys

Create a `.env` file in each project (never commit this to GitHub!):

```bash
OPENAI_API_KEY=your-key-here
HUGGINGFACE_TOKEN=your-token-here
PINECONE_API_KEY=your-key-here
```

Load it in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
```

Add `.env` to your `.gitignore`:
```bash
echo ".env" >> .gitignore
```

---

## 💻 5. Set Up Jupyter

```bash
pip install jupyterlab
jupyter lab
```

---

## 🆓 Free API Credits to Get

| Service | Free Tier | Sign Up |
|---------|-----------|---------|
| OpenAI | $5 free credit (new accounts) | https://platform.openai.com |
| Groq | Free generous limits | https://console.groq.com |
| HuggingFace | Free inference API | https://huggingface.co |
| Pinecone | 100K vectors free | https://pinecone.io |
| Cohere | 100 API calls/min free | https://cohere.com |
| Google Colab | Free GPU (T4) | https://colab.research.google.com |
| Kaggle Notebooks | Free GPU (P100, 30h/week) | https://kaggle.com |

---

## ✅ Verification

Run this to check everything is installed:

```python
import numpy; print("NumPy:", numpy.__version__)
import pandas; print("Pandas:", pandas.__version__)
import sklearn; print("Scikit-learn:", sklearn.__version__)
import torch; print("PyTorch:", torch.__version__)
import transformers; print("Transformers:", transformers.__version__)
import langchain; print("LangChain:", langchain.__version__)
import streamlit; print("Streamlit:", streamlit.__version__)
import fastapi; print("FastAPI:", fastapi.__version__)
print("\n✅ All libraries installed successfully!")
```
