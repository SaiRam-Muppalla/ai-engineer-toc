# Stage 1 — Python for AI

## 🎯 Learning Objectives

By the end of this stage you will:
- Write clean, Pythonic code for AI applications
- Master NumPy for numerical computing
- Use Pandas for data manipulation at scale
- Work with files, APIs, and external data sources
- Understand OOP patterns used in ML frameworks

## ⏱️ Estimated Time: 1.5 weeks

---

## 📐 Key Concepts

### Python Essentials
- List comprehensions, generators, decorators
- Classes and object-oriented programming
- Exception handling
- File I/O (CSV, JSON, text, PDF)
- Working with external libraries

### NumPy Deep Dive
- ndarray creation and manipulation
- Broadcasting rules
- Vectorized operations (no Python loops!)
- Random number generation for ML
- Linear algebra with `np.linalg`

### Pandas Deep Dive
- Series and DataFrame operations
- Loading data (CSV, JSON, Excel, SQL)
- Data cleaning and handling missing values
- Groupby, merge, join operations
- Time series handling

### Python for APIs
- `requests` library for HTTP calls
- Calling OpenAI / HuggingFace APIs
- Parsing JSON responses
- Rate limiting and error handling

---

## 🛠️ Tools & Technologies

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Core language |
| NumPy | 1.24+ | Numerical computing |
| Pandas | 2.0+ | Data manipulation |
| Requests | 2.31+ | HTTP calls |
| Jupyter | Latest | Interactive notebooks |

---

## 📚 Resources

See [resources.md](./resources.md) for full list. Key ones:

| Resource | Type | Link |
|----------|------|-------|
| Python for Everybody (Dr. Chuck) | YouTube | https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p |
| NumPy for Beginners (freeCodeCamp) | YouTube | https://www.youtube.com/watch?v=QUT1VHiLmmI |
| Pandas Tutorial (Corey Schafer) | YouTube Playlist | https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS |
| Official NumPy Docs | Documentation | https://numpy.org/doc/stable/ |
| Official Pandas Docs | Documentation | https://pandas.pydata.org/docs/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_python_basics.ipynb` — Python fundamentals refresher
- `02_numpy_exercises.ipynb` — 25 NumPy challenges
- `03_pandas_exercises.ipynb` — Data manipulation with real datasets
- `04_oop_for_ml.ipynb` — Build a mini ML pipeline class

---

## 🛠️ Mini Projects

1. **Data Pipeline Script** — Read CSV → clean → transform → export using Pandas
2. **API Data Fetcher** — Fetch data from a public API and save to structured format
3. **Pandas Profiler** — Build a function that auto-generates an EDA report for any CSV

---

## 🏆 Major Project

**AI Data Preprocessor Class**
- Build a reusable Python class for AI data preprocessing
- Features: handle missing values, encode categoricals, scale features, split data
- Write unit tests using `pytest`
- Package it as a proper Python module with `setup.py`
- Document with docstrings and a README

See [projects/](./projects/) for the starter code.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 4 exercises
- [ ] Built all 3 mini projects
- [ ] Completed the AI Data Preprocessor class project
- [ ] Written at least 10 unit tests
- [ ] Pushed to GitHub with a proper README

**Next Stage → [02 Data Analysis](../02-data-analysis/)**
