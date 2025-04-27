"""Tests for our load module."""

from pathlib import Path

from power_flow.load import get_data_from_csv


class TestLoadCsvData:
    def test_accepts_path_and_returns_data(self):
        """We can pass a path or a string and it's all good."""
        my_path = Path.cwd() / "data.csv"
        my_data = get_data_from_csv(my_path)
        assert isinstance(my_data, list)
        assert len(my_data) > 0
