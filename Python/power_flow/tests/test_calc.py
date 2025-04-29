"""Test for power flow analysis logic."""

import pytest
from pandas import DataFrame

from power_flow.calc import get_bus_mean_resistance


class TestGetBusMeanResistance:
    """Test for get_buses_out_of_range function."""

    bus_key = "bus_id"
    ohm_key = "resistance_pu"

    @pytest.fixture
    def lines(self):
        return DataFrame(
            {
                f"{self.bus_key}": [1, 2, 3, 4, 5, 6],
                f"{self.ohm_key}": [0.1, 0.3, 0.3, 0.1, 0.2, 0.6],
            }
        )

    def test_raises_error_with_invalid_key(self, lines):
        with pytest.raises(KeyError):
            _ = get_bus_mean_resistance(lines, bus_key="bad_key")
