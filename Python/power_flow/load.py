"""Utility functions for loading and marshaling the dataset.

In this practice file, we're using the pathlib library to handle
file paths in an OS-agnostic way. We're going to be using the pathlib
along with the pandas library and std=lib to load and marshal the dataset.
"""

import csv
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

# the Path class is one of the primary entry points for the pathlib module

# writing a path for a Windows system requires using backslashes.
# we can do this with raw strings or by using double backslashes
my_windows_path = Path("C:\\Users\\User\\Documents\\file.txt")
my_other_windows_path = Path(r"C:\Users\User\Documents\file.txt")

# We can create a path with forward slashes as and strings as the path components
# as long as there's at least one Path object in there
lines_csv = Path.cwd() / "data" / "lines.csv"

# We can also use the join path method
buses_csv = Path.cwd().joinpath("data", "buses.csv")


class PowerFlowAnalysisError(Exception):
    """General Error for when the power flow analysis fails."""


def get_data_from_csv(path: Path) -> list[dict]:
    """Read the entire file of data into memory.

    Returns:
        list of dictionaries with the parsed csv data, columns are keys.
    Raises:
        PowerFlowAnalysisError: If the file cannot be read.
    """
    try:
        data: list = []
        with path.open("r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for lines in csv_reader:
                data.append(lines)
        return data
    except FileNotFoundError as exc:
        msg = "file not found"
        logger.exception(msg, extra={"path": str(path)})
        raise PowerFlowAnalysisError(msg) from exc


def load_csv_to_df(path: Path) -> pd.DataFrame:
    """Load a dataset from a path into a pandas DataFrame.

    Returns:
        pandas DataFrame with the dataset.
    Raises:
        PowerFlowAnalysisError: if the file cannot be loaded.
    """
    if not path.exists():
        msg = "file not found"
        raise PowerFlowAnalysisError(msg)
    df = pd.read_csv(path)
    return df
