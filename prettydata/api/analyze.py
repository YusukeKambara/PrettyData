import collections
import pandas as pd
import numpy as np
import dateutil.parser
from datetime import datetime
from utils import utils


def analyze(df):
    """Analyze the each columns information about the DataFrame
    
    Arguments:
        df {pandas.DataFrame} -- DataFrame want to analyze
    
    Returns:
        [dict] -- Analyzing results
    """
    result = {"all_items": len(df)}
    if result["all_items"] <= 0: return {}
    df_converted = df.copy(deep=True)
    try:
        exec_start = datetime.now()
        for col in df.columns:
            # Initialize analyzing info
            result[col] = {
                "loss_rate": (float(df[col].isnull().sum()) / float(result["all_items"])) * 100,
                "unique_items": len(df[col].unique()),
                "allow_types": [str.__name__],
                "castable_items": {str.__name__: result["all_items"]}
            }
            items = result[col]["castable_items"]
            # Judge to be able to convert to datetime
            df_converted[col] = pd.to_datetime(df[col], errors="coerce")
            if df[col].isnull().sum() == df_converted[col].isnull().sum():
                result[col]["allow_types"].append(datetime.__name__)
            items[datetime.__name__] = df_converted[col].notnull().sum()
            # Judge to be able to convert to numeric
            df_converted[col] = pd.to_numeric(df[col], errors="coerce")
            if df[col].isnull().sum() == df_converted[col].isnull().sum():
                if df_converted[col].dtypes == "float64":
                    result[col]["allow_types"].append(float.__name__)
                elif df_converted[col].dtypes == "int64":
                    result[col]["allow_types"].append(int.__name__)
            items.update({"float": 0, "int": 0})
            if df_converted[col].dtypes == "float64":
                items["int"] = df_converted[col].dropna().apply(lambda x: x.is_integer()).astype("int").sum()
                items["float"] = df_converted[col].notnull().sum()
            elif df_converted[col].dtypes == "int64":
                items["int"] = df_converted[col].notnull().sum()
                items["float"] = items["int"]
    except Exception as e:
        result.update({"_error_message": e})
    finally:
        exec_finish = datetime.now()
        result.update({
            "_exec_start": exec_start.isoformat(),
            "_exec_finish": exec_finish.isoformat(),
            "_exec_time": str(exec_finish - exec_start),
            "_analyzed_items": len(result.keys())
        })
        return result
