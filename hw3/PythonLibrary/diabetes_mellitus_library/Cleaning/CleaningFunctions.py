# Code for computing hw3 project
import pandas as pd

def row_nan_removal(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df.dropna(subset = cols, inplace=True)
    return df

def mean_nan_fill(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df[col].fillna(df[col].mean(), inplace=True)
    return df


def dummy_creation(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df = pd.concat([df, pd.get_dummies(df[col])], axis = 1)
    return df

def binary_variable_generator(col: pd.Series, one_input: str, zero_input: str) -> pd.Series:
    return col.map({one_input: 1, zero_input: 0})
    