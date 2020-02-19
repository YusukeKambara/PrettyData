import collections
import pandas as pd
import numpy as np
from datetime import datetime
from utils import utils


def analyze(df):
    result = {}
    try:
        print("start: {}".format(datetime.now()))
        for col in df.columns:
            c = collections.Counter(df[col].map(type).to_list())
            result[col] = {
                "most_common_type": c.most_common()[0][0].__name__,
                "included_types": {val.__name__: c[val] for val in c.keys()},
                "loss_rate": (float(df[col].isnull().sum()) / float(len(df[col]))) * 100,
                "all_items": len(df[col]),
                "unique_items": len(df[col].unique())
            }
        print("finish: {}".format(datetime.now()))
    finally:
        return result

def recommend(df):
    return {}