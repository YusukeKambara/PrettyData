import collections
import pandas as pd
from datetime import datetime
from utils import utils

def analyze(df):
    row_count = len(df)
    result = {}
    for col in df.columns:
        values = df[col].to_list()
        c = collections.Counter([utils.judge_type(val) for val in values])
        result[col] = {
            "most_common_type": c.most_common()[0][0].__name__,
            "included_types": {val.__name__: c[val] for val in c.keys()},
            "loss_rate": (float(c[type(None)]) / float(row_count)) * 100,
            "all_items": len(values),
            "unique_items": len(set(values))
        }
    return result

def recommend(df):
    return {}