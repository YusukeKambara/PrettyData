import collections
import pandas as pd
from utils import utils


def diagnosis(file_path):
    print("Diagnosis file path: {}".format(file_path))
    df = pd.read_csv(file_path)
    row_count = len(df)
    print("File data row count: {}".format(str(row_count)))
    result = {}
    for col in df.columns:
        c = collections.Counter([
            type(val) if not pd.isnull(val) else type(None)
            for val in df[col].to_list()
        ])
        result[col] = {
            "most_common_type": c.most_common()[0],
            "included_types": c,
            "loss_rate": (float(c[type(None)]) / float(row_count)) * 100,
            "unique_items": len(set(df[col].to_list()))
            "castable_types": {
                "int": None,
                "float": None
            }
        }
    return result