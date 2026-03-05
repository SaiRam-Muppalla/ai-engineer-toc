# Stage 4 — Deep Learning

## 🎯 Learning Objectives

By the end of this stage you will:
- Understand how neural networks work (forward pass, backpropagation)
- Build and train CNNs for image classification
- Use RNNs and LSTMs for sequential data
- Understand the Transformer architecture
- Fine-tune pretrained models from HuggingFace
- Manage training runs with GPU acceleration

## ⏱️ Estimated Time: 2.5 weeks

---

## 📐 Key Concepts

### Neural Networks
- Perceptrons and multi-layer networks
- Activation functions: ReLU, sigmoid, tanh, softmax
- Loss functions: cross-entropy, MSE, focal loss
- Optimizers: SGD, Adam, AdamW
- Regularization: dropout, batch norm, weight decay
- Backpropagation and the chain rule

### Convolutional Neural Networks (CNNs)
- Convolution layers, pooling, padding
- Popular architectures: ResNet, VGG, EfficientNet, MobileNet
- Transfer learning and fine-tuning
- Data augmentation strategies

### Recurrent Neural Networks
- Vanilla RNN and the vanishing gradient problem
- LSTM and GRU — when to use them
- Sequence-to-sequence models
- Attention mechanism (intro)

### Transformers
- Self-attention mechanism
- BERT, GPT, ViT architectures overview
- Using HuggingFace `transformers` library
- Fine-tuning pretrained models

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| PyTorch | Primary deep learning framework |
| TensorFlow/Keras | Alternative framework |
| HuggingFace Transformers | Pretrained models |
| HuggingFace Datasets | Benchmark datasets |
| torchvision | Computer vision utilities |
| Weights & Biases (W&B) | Experiment tracking |
| CUDA | GPU acceleration |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| Neural Networks Zero to Hero (Karpathy) | YouTube Series | https://youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ |
| Deep Learning Specialization (Ng) | Coursera | https://www.coursera.org/specializations/deep-learning |
| PyTorch Tutorials | Official Docs | https://pytorch.org/tutorials/ |
| Fast.ai Practical DL | Free Course | https://course.fast.ai/ |
| The Annotated Transformer | Blog | https://nlp.seas.harvard.edu/annotated-transformer/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_neural_net_scratch.ipynb` — Build a 2-layer NN with NumPy only
- `02_pytorch_basics.ipynb` — PyTorch tensors, autograd, training loop
- `03_cnn_cifar10.ipynb` — Train a CNN on CIFAR-10
- `04_transfer_learning.ipynb` — Fine-tune ResNet on a custom dataset
- `05_text_classification.ipynb` — Sentiment analysis with BERT

---

## 🛠️ Mini Projects

1. **MNIST Digit Classifier** — Train a CNN that classifies handwritten digits
2. **Dog vs. Cat Classifier** — Transfer learning with MobileNet
3. **Sentiment Analysis API** — Fine-tune DistilBERT and serve with FastAPI

---

## 🏆 Major Project

### AI Image Classifier (Production Grade)

Build a complete image classification system with a web UI.

**Specs:**
- Choose a domain: medical X-rays, plant diseases, food, vehicles
- Collect or use an open dataset (10+ classes)
- Train a CNN from scratch **and** fine-tune a pretrained model
- Compare results with a training dashboard (W&B)
- Deploy as a FastAPI endpoint
- Build a drag-and-drop Streamlit UI
- Containerize with Docker

**Bonus:** Add Grad-CAM visualization to explain predictions.

See [projects/image-classifier/](./projects/) for the full project template.

---

## ✅ Stage Completion Checklist

- [ ] Built NN from scratch (NumPy only)
- [ ] Completed all 5 exercises
- [ ] Built the dog/cat classifier with transfer learning
- [ ] Fine-tuned a BERT model on a text classification task
- [ ] Completed and deployed the image classifier project
- [ ] Pushed everything to GitHub with W&B report linked

**Next Stage → [05 LLM Engineering](../05-llm-engineering/)**
