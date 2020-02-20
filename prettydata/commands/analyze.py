
import pandas as pd
from api import analyze as analyze_api


def analyze(file_path):
    df = pd.read_csv(file_path, dtype="object")
    # Analyze each column types of argument's DataFrame
    return analyze_api.analyze(df)

