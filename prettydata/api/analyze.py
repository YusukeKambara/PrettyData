import collections
import pandas as pd
from datetime import datetime
from utils import utils

def analyze(df):
    row_count = len(df)
    result = {}
    for col in df.columns:
        values = df[col].to_list()
        c = collections.Counter([
            type(val) if not pd.isnull(val) else type(None)
            for val in values
        ])
        result[col] = {
            "most_common_type": c.most_common()[0][0].__name__,
            "included_types": [val.__name__ for val in c.keys()],
            "loss_rate": (float(c[type(None)]) / float(row_count)) * 100,
            "unique_items": len(set(values)),
            "castable_types": {
                "tuple": collections.Counter([type(utils.safe_cast(val, tuple)) for val in values])[tuple],
                "list": collections.Counter([type(utils.safe_cast(val, list)) for val in values])[list],
                "datetime": collections.Counter([type(utils.safe_cast(val, datetime)) for val in values])[datetime],
                "int": collections.Counter([type(utils.safe_cast(val, int)) for val in values])[int],
                "float": collections.Counter([type(utils.safe_cast(val, float)) for val in values])[float],
                "str": collections.Counter([type(utils.safe_cast(val, str)) for val in values])[str]
            }
        }
    return result

def recommend(df):
    pass