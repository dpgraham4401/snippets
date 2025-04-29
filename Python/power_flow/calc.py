"""Calculations relevant to power flow analysis."""

import numpy as np
from pandas import DataFrame, Series
from pandas.core.groupby import DataFrameGroupBy


def get_bus_mean_resistance(
    lines: DataFrame,
    bus_key: str = "from_bus",
    ohm_key: str = "resistance_pu",
) -> Series:
    """Aggregate the resistance for outgoing lines and calculate the mean for each bus."""
    bus_by_id: DataFrameGroupBy = lines.groupby(bus_key)
    avg_resistance = bus_by_id[ohm_key].transform(np.mean)
    return avg_resistance
