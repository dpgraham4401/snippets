"""How to handle missing data in Python using pandas."""

import logging

import pandas as pd
from pandas import DataFrame

logger = logging.getLogger(__name__)

pd.options.mode.copy_on_write = "warn"


class SensorProcessError(Exception):
    """Error that occurs during sensor analysis."""


def read_csv_with_missing_data() -> DataFrame:
    """Read from sensor_readings.csv."""
    path = "./data/sensor_readings.csv"
    try:
        return pd.read_csv(path)
    except FileNotFoundError as exc:
        msg = "File not found"
        logger.exception(msg, extra={"file": path})
        raise SensorProcessError(msg) from exc


def fill_empty_with_average(data: DataFrame, name: str) -> DataFrame:
    """Create a dataframe with empty/NaN values filled with the column average.

    Note:
        starting in pandas > 3.0, modifying a copy or another reference of a dataframe
        will use Copy on Write (CoW) to avoid modifying the original dataframe.
        As long as we don't use .copy(deep=False), the original dataframe will be
        left unchanged. With 3.0, we just won't need to use the copy method, just assign.
    """
    data_copy = data.copy()
    avg = data_copy[name].mean()
    data_copy.fillna({name: avg}, inplace=True)  # noqa: PD002 # frowned upon
    return data_copy


def main():
    """Application entry point."""
    data = read_csv_with_missing_data()
    clean_data = fill_empty_with_average(data=data, name="temperature_c")
    print(clean_data.head())
    print(data.head())


if __name__ == "__main__":
    main()
