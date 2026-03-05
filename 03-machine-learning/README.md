# Stage 3 — Machine Learning Fundamentals

## 🎯 Learning Objectives

By the end of this stage you will:
- Understand and implement core ML algorithms
- Build end-to-end ML pipelines with Scikit-learn
- Properly evaluate and tune ML models
- Handle real-world ML challenges (imbalanced data, missing values, overfitting)
- Deploy a trained model as an API

## ⏱️ Estimated Time: 2 weeks

---

## 📐 Key Concepts

### Supervised Learning
| Algorithm | Use Case |
|-----------|---------|
| Linear Regression | Continuous value prediction |
| Logistic Regression | Binary/multi-class classification |
| Decision Trees | Explainable models |
| Random Forests | Tabular data, feature importance |
| Gradient Boosting (XGBoost, LightGBM) | Competition-winning models |
| Support Vector Machines | High-dimensional data |
| K-Nearest Neighbors | Simple baseline |

### Unsupervised Learning
| Algorithm | Use Case |
|-----------|---------|
| K-Means Clustering | Customer segmentation |
| DBSCAN | Anomaly detection |
| PCA | Dimensionality reduction, visualization |
| Hierarchical Clustering | Exploring group structure |

### Model Evaluation
- Train/validation/test split
- Cross-validation (k-fold, stratified)
- Metrics: accuracy, precision, recall, F1, AUC-ROC
- Confusion matrix analysis
- Regression metrics: MAE, MSE, RMSE, R²

### ML Pipeline Best Practices
- Feature engineering and selection
- Handling imbalanced classes (SMOTE, class weights)
- Hyperparameter tuning (GridSearchCV, RandomSearchCV, Optuna)
- Pipelines with Scikit-learn `Pipeline`
- Model persistence with `joblib`

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Scikit-learn | Core ML library |
| XGBoost | Gradient boosting |
| LightGBM | Fast gradient boosting |
| Optuna | Hyperparameter optimization |
| imbalanced-learn | Handle imbalanced datasets |
| joblib | Model saving/loading |
| SHAP | Model explainability |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| Scikit-learn User Guide | Official Docs | https://scikit-learn.org/stable/user_guide.html |
| StatQuest ML Playlist | YouTube | https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF |
| Krish Naik ML Course | YouTube | https://www.youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe |
| Hands-On ML Book | Book | https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_classification_pipeline.ipynb` — Build a full classification pipeline
- `02_regression_project.ipynb` — House price prediction with multiple models
- `03_clustering_analysis.ipynb` — Customer segmentation with K-Means
- `04_model_evaluation.ipynb` — Master confusion matrices, ROC curves, and CV

---

## 🛠️ Mini Projects

1. **Spam Email Classifier** — Classify emails as spam/not spam using TF-IDF + Logistic Regression
2. **Credit Risk Model** — Predict loan default with a gradient boosting model
3. **Customer Churn Predictor** — Telco churn dataset with SHAP explainability

---

## 🏆 Major Project

### Fake News Detector
Build a full ML system that classifies news articles as real or fake.

**Features:**
- Text preprocessing (tokenization, stopword removal, TF-IDF, word embeddings)
- Train multiple classifiers (Logistic Regression, Random Forest, XGBoost)
- Compare models with proper cross-validation
- SHAP explainability: show which words influenced the prediction
- Serve as a REST API with FastAPI
- Build a Streamlit UI where users paste article text and get predictions

**Dataset:** [Fake News Dataset on Kaggle](https://www.kaggle.com/c/fake-news)

See [projects/fake-news-detector/](./projects/) for complete starter code.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 4 exercises
- [ ] Built the spam email classifier
- [ ] Built the credit risk model
- [ ] Completed the fake news detector
- [ ] Deployed the fake news detector as an API
- [ ] Pushed everything to GitHub

**Next Stage → [04 Deep Learning](../04-deep-learning/)**
