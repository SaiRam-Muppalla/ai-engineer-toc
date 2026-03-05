# Fake News Detector

An end-to-end ML system that classifies news articles as real or fake.

## 📋 Project Overview

**Tech Stack:** Python, Scikit-learn, XGBoost, SHAP, FastAPI, Streamlit

**Dataset:** [Fake and Real News Dataset (Kaggle)](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

## 🏗️ Architecture

```
Raw Text → Preprocessing → TF-IDF Features → Model → Prediction
                                                    ↓
                                              SHAP Explanation
```

## 🚀 Getting Started

```bash
pip install -r requirements.txt

# Train the model
python train.py

# Start the API
uvicorn api:app --reload

# Start the UI
streamlit run app.py
```

## 📁 Files

| File | Description |
|------|-------------|
| `train.py` | Model training script |
| `api.py` | FastAPI prediction endpoint |
| `app.py` | Streamlit web interface |
| `model.pkl` | Saved trained model |
| `vectorizer.pkl` | Saved TF-IDF vectorizer |
| `notebook.ipynb` | Full EDA and modeling notebook |

## 📊 Results

| Model | Accuracy | F1 Score | AUC-ROC |
|-------|----------|----------|---------|
| Logistic Regression | 98.2% | 0.982 | 0.998 |
| Random Forest | 98.7% | 0.987 | 0.999 |
| XGBoost | 99.1% | 0.991 | 0.999 |
