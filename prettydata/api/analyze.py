import collections
import pandas as pd
import numpy as np
from datetime import datetime
from utils import utils


def analyze(df):
    result = {}
    try:
        for col in df.columns:
            # Initialize analyzing info
            result[col] = {
                "loss_rate": (float(df[col].isnull().sum()) / float(len(df[col]))) * 100,
                "all_items": len(df[col]),
                "unique_items": len(df[col].unique()),
                "allow_types": [],
                "allow_types_without_na": []
            }
            # Judge to be able to convert to datetime
            try:
                pd.to_datetime(df[col])
                result[col]["allow_types"].append(datetime.__name__)
                result[col]["allow_types_without_na"].append(datetime.__name__)
            except:
                try:
                    pd.to_datetime(df[col].dropna())
                    result[col]["allow_types_without_na"].append(datetime.__name__)
                except:
                    pass
            # Judge to be able to convert to float
            try:
                if (df[col] == df[col].map(float).map(str)).all(): raise
                result[col]["allow_types"].append(float.__name__)
                result[col]["allow_types_without_na"].append(float.__name__)
            except:
                try:
                    if (df[col] == df[col].dropna().map(float).map(str)).all(): raise
                    result[col]["allow_types_without_na"].append(float.__name__)
                except:
                    pass
            # Judge to be able to convert to int
            try:
                if (df[col] == df[col].map(int).map(str)).all(): raise
                result[col]["allow_types"].append(int.__name__)
                result[col]["allow_types_without_na"].append(int.__name__)
            except:
                try:
                    if (df[col] == df[col].dropna().map(int).map(str)).all(): raise
                    result[col]["allow_types_without_na"].append(int.__name__)
                except:
                    pass
            # Judge to be able to convert to str
            try:
                df[col].map(str)
                result[col]["allow_types"].append(str.__name__)
                result[col]["allow_types_without_na"].append(str.__name__)
            except:
                try:
                    df[col].dropna().map(str)
                    result[col]["allow_types_without_na"].append(str.__name__)
                except:
                    pass
    finally:
        return result

def recommend(df):
    return {}

def judge_type(val):
    if str(val).isdigit(): return int
    elif str(val).replace(".", "").isdigit(): return float
    else: return str