# Linear Regression from Scratch

A complete implementation of linear regression using only NumPy — no Scikit-learn.

## 📖 What You'll Learn

- Derive the cost function (Mean Squared Error)
- Implement gradient descent manually
- Vectorize the computations with NumPy
- Plot training curves
- Evaluate using R², MAE, and RMSE

## 🚀 Getting Started

```bash
pip install numpy matplotlib pandas
jupyter notebook linear_regression.ipynb
```

## 📁 Files

| File | Description |
|------|-------------|
| `linear_regression.ipynb` | Main notebook with full implementation |
| `data/housing.csv` | California Housing dataset sample |

## 🧮 Math Background

**Model:** `ŷ = Xw + b`

**Cost function (MSE):**
```
J(w, b) = (1/2m) * Σ(ŷᵢ - yᵢ)²
```

**Gradient update:**
```
w := w - α * (∂J/∂w)
b := b - α * (∂J/∂b)
```

Where:
```
∂J/∂w = (1/m) * Xᵀ(Xw - y)
∂J/∂b = (1/m) * Σ(Xw - y)
```
