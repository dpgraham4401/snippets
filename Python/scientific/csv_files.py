"""Reading a writing CSV files refresher.

An overview of the options for reading/writing CSV files
using the std lib csv files or pandas.
"""

# Using the standard library csv package

import csv
import logging

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

logger = logging.getLogger(__name__)


class MyCsvError(Exception):
    """Custom exception we expose as part of our packages API."""


def read_mini_without_headers() -> None:
    """Read a mini CSV file that does not contain a header (OHH NOW)."""
    with open("./data/mini_no_headers.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=("foo", "bar", "baz", "fee", "fii"))
        tie_count: dict[str, int] = {}
        for row in csv_reader:
            tie_name = row["baz"]
            if tie_name in tie_count:
                tie_count[tie_name] += 1
            else:
                tie_count[tie_name] = 1


my_data = [["Joe", "smith", "21", "hiking"], ["samantha", "adams", "42", "swimming"]]


def writing_example_csv_data() -> None:
    with open("./data/example.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for data in my_data:
            writer.writerow(data)


def reading_large_data_with_pandas() -> None:
    """reading a file with pandas is wicked simple, just...

    We can replace the header names with our own by telling pandas both the num headers
    and the column names.
    """
    df = pd.read_csv(
        "./data/five_min_tie_flows.csv",
        header=0,
        names=["date_added", "date_updated", "union", "watts", "power"],
        dtype={
            "date_added": str,
            "date_updated": str,
            "union": str,
            "watts": np.float64,
            "power": np.float64,
        },
        parse_dates=["date_added", "date_updated"],
    )
    # We can use boolean operators to filter, while doing analysis on additional columns
    # This filters rows where union is CPLE, then sums the watts' column
    cple_watts = df.loc[df["union"] == "CPLE", "watts"]
    print(f"{cple_watts.mean()}")
    print(f"{cple_watts.max()}")
    print(f"{cple_watts.min()}")


def load_simulation_data() -> DataFrame:
    """Load sample dataset via hardcoded filepath."""
    try:
        return pd.read_csv("./data/simulation.csv")
    except pd.errors.ClosedFileError as e:
        msg = "error reading data."
        logger.exception(msg, exc_info=e)
        raise MyCsvError(msg) from e


def filter_invalid_results(df: DataFrame) -> DataFrame:
    """Filter rows that cannot be used for the analysis."""
    valid_data = df[df["valid"]]
    return valid_data.dropna(subset=["temperature", "pressure"])


def get_the_mean_temp(data: DataFrame) -> float:
    """pandas provides methods for calculating statis like the mean, median, for a series/column."""
    _median = data["temperature"].median()
    _mode = data["temperature"].mode()
    return data["temperature"].mean()


def get_mean_simulation_pressure(data: DataFrame) -> Series:
    """Using the groupby method.

    We group all the rows with the same value in the simulation_id col.
    """
    try:
        simulations = data.groupby("simulation_id")
        return simulations["pressure"].mean()
    except KeyError as exc:
        msg = "error calculating mean."
        logger.exception(msg, exc_info=exc)
        raise MyCsvError(msg) from exc


def add_calculated_density(data: DataFrame) -> DataFrame:
    """Calculate the density based on the assumption that it's an ideal gas"""
    data["density"] = data["pressure"] / (
        data["temperature"] * 1.8
    )  # not correct, but ok for example
    return data


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert celsius to fahrenheit."""
    return celsius * (9 / 5) + 32


def add_calculated_fahrenheit(data: DataFrame) -> DataFrame:
    """Using the apply method

    If we need a more complex method of producing a series of data.
    It's best to avoid using the apply method since, under the hoo, it uses
    a python for loop, and tends to avoid the vectorized operations that pandas
    uses to stay performant.
    """
    data["fahrenheit"] = data.apply(lambda row: celsius_to_fahrenheit(row["temperature"]), axis=1)
    return data


if __name__ == "__main__":
    raw_data = load_simulation_data()
    clean_data = filter_invalid_results(raw_data)
    temp = get_the_mean_temp(clean_data)
    simulation_temperature = get_mean_simulation_pressure(clean_data)
    data_with_density = add_calculated_density(clean_data)
    data_with_fahrenheit = add_calculated_fahrenheit(data_with_density)
    print(data_with_density.head())
