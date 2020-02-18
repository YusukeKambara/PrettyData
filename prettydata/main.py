from pprint import pprint
import click
import pandas as pd
from commands import analyze as command_analyze

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

if __name__ == "__main__":
    main()