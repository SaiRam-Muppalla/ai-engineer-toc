# AI Image Classifier (Production Grade)

An end-to-end image classification system with a web UI, built for production.

## 📋 Project Overview

Build an image classifier for a domain of your choice. This template uses **plant disease detection** as an example.

**Tech Stack:** PyTorch, torchvision, FastAPI, Streamlit, Docker, Weights & Biases

## 🏗️ Architecture

```
Image Upload (Streamlit) → FastAPI → PyTorch Model → Prediction + Grad-CAM
```

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train.py --data_dir ./data --epochs 20 --model resnet50

# Start API
uvicorn api:app --host 0.0.0.0 --port 8000

# Start UI
streamlit run app.py

# Docker
docker compose up
```

## 📁 Project Structure

```
image-classifier/
├── data/                    # Dataset (not committed)
├── models/                  # Saved models
├── notebooks/
│   └── exploration.ipynb    # EDA and prototyping
├── src/
│   ├── dataset.py           # Custom PyTorch Dataset
│   ├── model.py             # Model architecture
│   ├── train.py             # Training loop
│   ├── evaluate.py          # Evaluation metrics
│   └── gradcam.py           # Grad-CAM visualization
├── api.py                   # FastAPI endpoint
├── app.py                   # Streamlit UI
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 📊 Expected Results

| Model | Accuracy | Training Time (GPU) |
|-------|----------|-------------------|
| CNN from scratch | ~82% | ~30 min |
| ResNet50 (fine-tuned) | ~96% | ~15 min |
| EfficientNet-B3 | ~97% | ~20 min |
