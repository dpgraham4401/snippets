"""Reading a writing CSV files refresher.

An overview of the options for reading/writing CSV files
using the std lib csv files or pandas.
"""

# Using the standard library csv package

import csv

import numpy as np
import pandas as pd


def read_mini_without_headers() -> None:
    """Read a mini CSV file that does not contain a header (OHH NOW)."""
    with open("./data/mini_no_headers.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=("foo", "bar", "baz", "fee", "fii"))
        tie_count: dict[str, int] = {}
        for row in csv_reader:
            tie_name = row["baz"]
            if tie_name in tie_count:
                tie_count[tie_name] += 1
            else:
                tie_count[tie_name] = 1


my_data = [["Joe", "smith", "21", "hiking"], ["samantha", "adams", "42", "swimming"]]


def writing_example_csv_data() -> None:
    with open("./data/example.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for data in my_data:
            writer.writerow(data)


def reading_large_data_with_pandas() -> None:
    """reading a file with pandas is wicked simple, just...

    We can replace the header names with our own by telling pandas both the num headers
    and the column names.
    """
    df = pd.read_csv("./data/five_min_tie_flows.csv",
        header=0,
        names=["date_added", "date_updated", "union", "watts", "power"],
        dtype={"date_added": str,"date_updated": str,"union": str,"watts": np.float64,"power": np.float64},
        parse_dates=["date_added", "date_updated"],
    )
    # We can use boolean operators to filter, while doing analysis on additional columns
    # This filters rows where union is CPLE, then sums the watts' column
    cple_watts = df.loc[df["union"] == "CPLE", "watts"]
    print(f"{cple_watts.mean()}")
    print(f"{cple_watts.max()}")
    print(f"{cple_watts.min()}")


if __name__ == "__main__":
    reading_large_data_with_pandas()
