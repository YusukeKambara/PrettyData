
import pandas as pd
from api import analyze as analyze_api
from api import recommend as recommend_api

def recommend(file_path):
    analyzed_results = analyze_api(file_path)
    recommeded_results = recommend_api(analyzed_results)