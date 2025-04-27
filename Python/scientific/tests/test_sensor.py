"""Test for the 'sensor analysis' practice."""

import numpy as np
from pandas import DataFrame

from scientific.sensor_analysis import fill_empty_with_average


class TestCleanData:
    def test_fill_returns_a_dataframe(self):
        col_name = "a"
        df = DataFrame({col_name: [1, 2, 3, np.nan, 4]})
        cleaned_data = fill_empty_with_average(df, col_name)
        assert isinstance(cleaned_data, DataFrame)

    def test_fill_empty_with_average(self):
        col_name = "a"
        df = DataFrame({col_name: [1, 2, 3, np.nan, 4]})
        cleaned_data = fill_empty_with_average(df, col_name)
        for element in cleaned_data[col_name]:
            assert element is not None

    def test_does_not_fill_other_columns(self):
        col_name = "a"
        other_col_name = "b"
        df = DataFrame({col_name: [1, 2, 3, np.nan, 4], other_col_name: [5, np.nan, 7, np.nan, 9]})
        other_col = fill_empty_with_average(df, col_name)[other_col_name]
        has_nan = np.isnan(other_col)
        assert np.any(has_nan)

    def test_creates_copy_of_dataframe(self):
        col_name = "a"
        data = DataFrame({col_name: [1, 2, 3, np.nan, 4]})
        cleaned_data = fill_empty_with_average(data, col_name)
        assert data is not cleaned_data
