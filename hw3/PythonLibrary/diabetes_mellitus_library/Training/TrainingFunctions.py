# Code for computing hw3 project
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def split_data(df: pd.DataFrame, target_col: str, predictor_cols: list) -> (pd.DataFrame, pd.DataFrame, pd.Series, pd.Series):
    X = df[predictor_cols]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_logistic_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    logistic_model = LogisticRegression()
    logistic_model.fit(X_train, y_train)
    return logistic_model

def predict(model: LogisticRegression, X: pd.DataFrame) -> np.ndarray:
    pred = model.predict_proba(X)
    return pred[:, 1]

def get_roc_auc(y: pd.Series, y_probs: pd.Series) -> np.float64:
    return roc_auc_score(y, y_probs)
