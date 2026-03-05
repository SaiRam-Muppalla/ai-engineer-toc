"""
AI Data Preprocessor — reusable class for AI/ML data preprocessing.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder


class AIDataPreprocessor:
    """
    A reusable preprocessor for AI/ML datasets.

    Handles:
    - Missing value imputation
    - Categorical encoding
    - Feature scaling
    - Train/val/test splitting
    """

    def __init__(self, test_size: float = 0.2, val_size: float = 0.1,
                 scaler_type: str = 'standard', random_state: int = 42):
        self.test_size = test_size
        self.val_size = val_size
        self.scaler_type = scaler_type
        self.random_state = random_state
        self.scaler = StandardScaler() if scaler_type == 'standard' else None
        self.label_encoders: dict = {}
        self.feature_names: list = []

    def fit_transform(self, df: pd.DataFrame, target: str):
        """Full preprocessing pipeline."""
        df = df.copy()

        # Separate features and target
        y = df[target]
        X = df.drop(columns=[target])

        # Handle missing values
        X = self._handle_missing(X)

        # Encode categoricals
        X = self._encode_categoricals(X)
        self.feature_names = list(X.columns)

        # Split
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state)
        val_ratio = self.val_size / (1 - self.test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_ratio, random_state=self.random_state)

        # Scale
        if self.scaler:
            X_train = self.scaler.fit_transform(X_train)
            X_val = self.scaler.transform(X_val)
            X_test = self.scaler.transform(X_test)

        return X_train, X_val, X_test, y_train, y_val, y_test

    def _handle_missing(self, X: pd.DataFrame) -> pd.DataFrame:
        for col in X.columns:
            if X[col].isnull().any():
                if X[col].dtype in [np.float64, np.int64]:
                    X[col] = X[col].fillna(X[col].median())
                else:
                    X[col] = X[col].fillna(X[col].mode()[0])
        return X

    def _encode_categoricals(self, X: pd.DataFrame) -> pd.DataFrame:
        cat_cols = X.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            self.label_encoders[col] = le
        return X
