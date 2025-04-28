"""Main entry point for the practice exercise."""

from pathlib import Path

from power_flow.clean import get_buses_out_of_range
from power_flow.load import load_csv_to_df


def main():
    """Script for executing the power flow analysis tool.

    Hardcodes the inputs, consider adding a CLI.
    """
    buses_data_source = Path.cwd() / "data" / "buses.csv"
    lines_data_source = Path.cwd() / "data" / "lines.csv"
    buses_data = load_csv_to_df(buses_data_source)
    lines_data = load_csv_to_df(lines_data_source)
    filtered_buses = get_buses_out_of_range(buses_data, col="voltage_pu", val_range=(0.9, 1.1))


if __name__ == "__main__":
    main()
