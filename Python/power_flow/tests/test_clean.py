"""Tests for the data validation and cleaning module."""

import pandas as pd
import pytest

from power_flow.clean import filter_buses_by_id, get_buses_out_of_range


class TestGetOutOfRangeValues:
    @pytest.fixture
    def data(self):
        return pd.DataFrame(
            {"col_name": [1, 9, 10, 15, 3], "alt_col": ["foo", "bar", "baz", "blip", "chits"]}
        )

    def test_raises_error_when_col_empty(self, data):
        with pytest.raises(ValueError, match="col"):
            _ = get_buses_out_of_range(data, val_range=(1, 2))

    def test_raises_error_when_range_empty(self, data):
        with pytest.raises(ValueError, match="val_range"):
            _ = get_buses_out_of_range(data, col="foo")

    def test_filter_rows_with_col_outside_range(self, data):
        bottom = 7
        top = 16
        filtered_data = get_buses_out_of_range(data, col="col_name", val_range=(bottom, top))
        for element in filtered_data["col_name"]:
            assert element < bottom or element > top


class TestFilterByBusId:
    @pytest.fixture
    def data(self):
        return pd.DataFrame(
            {"bus_id": [1, 2, 3, 4, 5], "alt_col": ["foo", "bar", "baz", "blip", "chits"]}
        )

    def test_returns_dataframe_with_correct_number_of_rows(self, data):
        original_length = len(data.index)
        ids = [1, 2]
        filtered_data = filter_buses_by_id(data, ids)
        assert len(filtered_data.index) == original_length - len(ids)
        print(filtered_data)
