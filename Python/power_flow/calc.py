"""Calculations relevant to power flow analysis."""

from pandas import DataFrame


def get_bus_mean_resistance(
    lines: DataFrame,
    bus_key: str = "bus_id",
    ohm_key: str = "resistance_pu",
) -> DataFrame:
    """Aggregate the resistance for outgoing lines and calculate the mean for each bus."""
    bus_by_id = lines.groupby(bus_key)
    print(bus_by_id.h)
    return lines
