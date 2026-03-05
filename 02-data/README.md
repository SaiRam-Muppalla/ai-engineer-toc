# Stage 2 — Data Engineering, Analysis & Visualization

## 🎯 Learning Objectives

By the end of this stage you will:
- Understand data engineering fundamentals (ETL, pipelines, data quality)
- Write SQL queries to extract and transform data
- Perform exploratory data analysis (EDA) on real-world datasets
- Clean messy, real-world data confidently
- Engineer meaningful features from raw data
- Create professional visualizations that tell a story
- Apply statistical tests to validate insights

## ⏱️ Estimated Time: 1.5 weeks

---

## 📐 Key Concepts

### Data Engineering Fundamentals

| Concept | Description |
|---------|-------------|
| ETL Pipelines | Extract data from sources → Transform (clean, aggregate) → Load into a destination |
| Data Warehousing | Central repository for structured data optimized for analytics |
| Data Lakes | Storage for raw, unstructured data (S3, GCS, Azure Blob) |
| Batch vs Streaming | Batch for periodic jobs; streaming for real-time (Kafka, Pub/Sub) |
| Data Quality | Validation, schema checks, completeness, consistency |
| Data Versioning | Track dataset versions for reproducibility (DVC, Delta Lake) |

**SQL for Data Engineering:**
- Writing complex queries: JOINs, CTEs, window functions
- Aggregations for reporting and feature computation
- Indexing and query optimization basics
- Tools: PostgreSQL, SQLite, BigQuery, DuckDB

**Python Data Pipelines:**
- Reading from multiple sources (CSV, JSON, SQL, APIs)
- Transforming data with Pandas and SQL
- Scheduling with cron or workflow tools (Airflow concepts)
- Data validation with Great Expectations or Pandera

### Exploratory Data Analysis (EDA)
- Understanding data types, distributions, and shapes
- Detecting outliers with IQR and z-scores
- Correlation analysis
- Missing value analysis and strategies
- Class imbalance detection

### Feature Engineering
- Creating new features from existing ones
- Date/time feature extraction
- Text feature extraction (word count, TF-IDF basics)
- Binning and discretization
- Interaction features

### Data Visualization
- Distribution plots: histograms, KDE, box plots
- Relationship plots: scatter, heatmap, pairplot
- Categorical plots: bar, count, violin
- Time-series plots
- Creating clear, publication-ready charts with Matplotlib & Seaborn

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| SQL (PostgreSQL / SQLite / DuckDB) | Data querying and transformation |
| Matplotlib | Low-level plotting |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| ydata-profiling | Automated EDA reports |
| Great Expectations / Pandera | Data validation |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| Seaborn Tutorial | Official Docs | https://seaborn.pydata.org/tutorial.html |
| Matplotlib Tutorials | Official Docs | https://matplotlib.org/stable/tutorials/index.html |
| Kaggle EDA Courses | Kaggle Learn | https://www.kaggle.com/learn/data-visualization |
| Plotly Docs | Official Docs | https://plotly.com/python/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_eda_titanic.ipynb` — Full EDA on the Titanic dataset
- `02_feature_engineering.ipynb` — Engineer features from the Ames Housing dataset
- `03_visualization_challenge.ipynb` — Recreate 10 charts from scratch

---

## 🛠️ Mini Projects

1. **EDA Report Generator** — A Python script that takes any CSV and outputs a full HTML EDA report
2. **Data Quality Checker** — A tool that automatically flags data quality issues in a dataset

---

## 🏆 Major Project

**Sales Analytics Dashboard**
- Dataset: Superstore Sales (publicly available on Kaggle)
- Perform complete EDA
- Engineer features: month, quarter, profit margin, etc.
- Build 10+ visualizations
- Find 5 actionable business insights
- Export to an interactive Plotly/Streamlit dashboard

See [projects/](./projects/) for starter code and data.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 3 exercises
- [ ] Built the EDA report generator
- [ ] Completed the Sales Analytics Dashboard
- [ ] Can perform EDA on a new dataset in under 30 minutes
- [ ] Pushed to GitHub with screenshots

**Next Stage → [03 Machine Learning](../03-machine-learning/)**
