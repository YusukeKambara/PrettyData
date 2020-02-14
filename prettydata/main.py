from pprint import pprint
import click
import pandas as pd
from commands import dx as command_dx

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
def dx(file_path):
    """Diagnosis the data quality
    """
    df = command_dx.diagnosis(file_path)
    pprint(df)

if __name__ == "__main__":
    main()