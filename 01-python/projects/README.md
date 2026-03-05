# AI Data Preprocessor

A reusable Python class for AI data preprocessing.

## Features

- Handle missing values (drop, fill with mean/median/mode)
- Encode categorical variables (label encoding, one-hot encoding)
- Scale features (StandardScaler, MinMaxScaler)
- Train/validation/test split
- Save and load preprocessing state

## Usage

```python
from preprocessor import AIDataPreprocessor

prep = AIDataPreprocessor()
X_train, X_val, X_test, y_train, y_val, y_test = prep.fit_transform(df, target='price')
```

## Files

| File | Description |
|------|-------------|
| `preprocessor.py` | Main class implementation |
| `tests/test_preprocessor.py` | Unit tests with pytest |
| `demo.ipynb` | Usage demo with Titanic dataset |
