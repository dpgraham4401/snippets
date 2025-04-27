"""Tests for our load module."""

from pathlib import Path

import pandas as pd
import pytest

from power_flow.load import PowerFlowAnalysisError, get_data_from_csv, load_csv_to_df


class TestLoadCsvData:
    def test_accepts_path_and_returns_data(self):
        """We can pass a path or a string and it's all good."""
        my_path = Path.cwd() / "data.csv"
        my_data = get_data_from_csv(my_path)
        assert isinstance(my_data, list)
        assert len(my_data) > 0

    def test_errors_when_file_does_not_exists(self):
        """We raise a custom exception as aprt of our package API."""
        my_path = Path.cwd() / "foo.csv"
        with pytest.raises(PowerFlowAnalysisError):
            _ = get_data_from_csv(my_path)


class TestLoadDataIntoDataFrame:
    @pytest.fixture
    def data_path(self) -> Path:
        return Path.cwd() / "data.csv"

    def test_returns_dataframe(self, data_path):
        """Returns an instance of the pandas libray dataframe."""
        df = load_csv_to_df(data_path)
        assert isinstance(df, pd.DataFrame)

    def test_raises_error_if_file_not_found(self):
        path = Path.cwd() / "foo.csv"
        with pytest.raises(PowerFlowAnalysisError):
            _ = load_csv_to_df(path)
