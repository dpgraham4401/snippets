"""Module containing logic necessary to validate power flow analysis datasets."""

from pandas import DataFrame


def get_buses_out_of_range(
    data: DataFrame,
    *,
    col: str | None = None,
    val_range: tuple[float, float] | None = None,
) -> DataFrame:
    """Get view of values out of bound.

    Returns:
        A new dataframe with the values in the specified column that are outside
        the range.

    Raises:
        ValueError: If `col` is not a valid column name.
        ValuesError: if `col` or `val_range` is not provided.
    """
    if col is None:
        msg = "col must be provided."
        raise ValueError(msg)
    if val_range is None:
        msg = "val_range must be provided."
        raise ValueError(msg)
    results = data.copy()
    return results[~results[col].between(*val_range)]


def filter_buses_by_id(data: DataFrame, ids: list[int]) -> DataFrame:
    """Remove rows from the dataframe by bus ID.

    Returns:
        A new dataframe with the bus IDs removed.
    """
    results = data.copy()
    return results[~results["bus_id"].isin(ids)]
