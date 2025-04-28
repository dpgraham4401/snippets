"""Tests for the data validation and cleaning module."""

import pandas as pd
import pytest

from power_flow.clean import get_buses_out_of_range


class TestFilterColByRange:
    @pytest.fixture
    def data(self):
        return pd.DataFrame(
            {"col_name": [1, 9, 10, 15, 3], "alt_col": ["foo", "bar", "baz", "blip", "chits"]}
        )

    def test_raises_error_when_col_empty(self, data):
        with pytest.raises(ValueError):
            _ = get_buses_out_of_range(data, val_range=(1, 2))

    def test_raises_error_when_range_empty(self, data):
        with pytest.raises(ValueError):
            _ = get_buses_out_of_range(data, col="foo")

    def test_filter_rows_with_col_outside_range(self, data):
        bottom = 7
        top = 16
        filtered_data = get_buses_out_of_range(data, col="col_name", val_range=(bottom, top))
        for element in filtered_data["col_name"]:
            assert element < bottom or element > top
