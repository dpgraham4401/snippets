"""How to handle missing data in Python using pandas."""

import logging

import pandas as pd
from pandas import DataFrame

logger = logging.getLogger(__name__)


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


if __name__ == "__main__":
    data = read_csv_with_missing_data()
    print(data.head())
