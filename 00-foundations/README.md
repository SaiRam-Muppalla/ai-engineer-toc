# Stage 0 — Foundations (Math + Programming)

## 🎯 Learning Objectives

By the end of this stage you will:
- Understand the core math concepts that power AI algorithms
- Comfortably work with vectors, matrices, and derivatives
- Apply probability and statistics to data problems
- Write clean, efficient Python code

## ⏱️ Estimated Time: 2 weeks

---

## 📐 Key Concepts

### Linear Algebra
| Concept | Why It Matters in AI |
|---------|----------------------|
| Vectors & Matrices | Represent data, weights, and transformations |
| Matrix multiplication | Forward pass in neural networks |
| Dot product | Similarity, attention scores |
| Eigenvalues & Eigenvectors | PCA, dimensionality reduction |
| Norms | Regularization, loss functions |

### Calculus
| Concept | Why It Matters in AI |
|---------|----------------------|
| Derivatives | Gradient of the loss function |
| Chain rule | Backpropagation |
| Partial derivatives | Multi-variable optimization |
| Gradient descent | Training neural networks |

### Statistics & Probability
| Concept | Why It Matters in AI |
|---------|----------------------|
| Mean, Median, Variance | Describing datasets |
| Probability distributions | Modeling uncertainty |
| Bayes' theorem | Bayesian ML, NLP |
| Hypothesis testing | Evaluating model performance |
| Correlation & covariance | Feature relationships |

---

## 🛠️ Tools & Technologies

- Python 3.10+
- NumPy (for matrix operations)
- Matplotlib (for visualizing math concepts)
- Jupyter Notebook

---

## 📚 Resources

See [resources.md](./resources.md) for full list. Key ones:

| Resource | Type | Link |
|----------|------|-------|
| 3Blue1Brown — Essence of Linear Algebra | YouTube Series | https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab |
| 3Blue1Brown — Essence of Calculus | YouTube Series | https://youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr |
| StatQuest with Josh Starmer | YouTube Channel | https://www.youtube.com/c/joshstarmer |
| Khan Academy Linear Algebra | Free Course | https://www.khanacademy.org/math/linear-algebra |
| Mathematics for Machine Learning (book) | Free PDF | https://mml-book.github.io/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_vectors_matrices.ipynb` — Vector and matrix operations with NumPy
- `02_derivatives_gradients.ipynb` — Computing derivatives and gradients manually
- `03_probability_statistics.ipynb` — Probability distributions and statistics
- `04_gradient_descent.ipynb` — Implement gradient descent from scratch

---

## 🛠️ Mini Projects

1. **Math Visualizer** — Build a Python tool that visualizes vectors, matrix transformations, and gradient descent in 2D
2. **Statistics Dashboard** — Load a CSV dataset and compute/display all key statistics

---

## 🏆 Major Project

**Linear Regression from Scratch**
- Implement linear regression using only NumPy (no Scikit-learn)
- Use gradient descent to minimize the loss
- Visualize the training loss curve
- Evaluate on a real dataset (e.g., Boston Housing, California Housing)
- Document your math derivations in the README

See [projects/linear_regression_from_scratch/](./projects/) for the starter code.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 4 exercises
- [ ] Built the math visualizer mini project
- [ ] Completed the linear regression from scratch project
- [ ] Can explain backpropagation math in simple terms
- [ ] Pushed all work to your GitHub

**Next Stage → [01 Python for AI](../01-python-for-ai/)**
