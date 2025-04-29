"""Test for power flow analysis logic."""

import pytest
from pandas import DataFrame, Series

from power_flow.calc import bus_mean_resistance


class TestGetBusMeanResistance:
    """Test for get_buses_out_of_range function."""

    bus_key = "from_bus"
    ohm_key = "resistance_pu"

    @pytest.fixture
    def lines(self):
        return DataFrame(
            {
                f"{self.bus_key}": [1, 1, 2, 3, 3, 3],
                f"{self.ohm_key}": [0.1, 0.3, 0.3, 0.1, 0.2, 0.6],
            }
        )

    def test_raises_error_with_invalid_key(self, lines):
        with pytest.raises(KeyError):
            _ = bus_mean_resistance(lines, bus_key="bad_key")

    def test_returns_a_dataframe_of_bus_id_and_avg_resistance(self, lines):
        results = bus_mean_resistance(lines)
        assert isinstance(results, Series)
