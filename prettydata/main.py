from pprint import pprint
import click
import pandas as pd
from commands import analyze as command_analyze
from commands import recommend as command_recommend

pd.set_option("display.max_columns", None)

def main():
    cmd()

@click.group()
def cmd():
    """First layer sub-command group
    """
    pass

@cmd.command()
@click.argument("file_path", type=click.Path(exists=True))
def analyze(file_path):
    """Analyze the data quality
    """
    df = command_analyze.analyze(file_path)
    pprint(df)

@cmd.command()
@click.argument("file_path", type=click.Path(exists=True))
def recommend(file_path):
    """Recommend of the best type at each column based on [analyze] command results
    """
    analyzed_results = analyze(file_path)
    recommended_result = command_recommend(analyzed_results)

if __name__ == "__main__":
    main()