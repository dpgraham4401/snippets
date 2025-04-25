"""Reading a writing CSV files refresher.

An overview of the options for reading/writing CSV files
using the std lib csv files or pandas.
"""

# Using the standard library csv package

import csv

import pandas
import pandas as pd

def read_mini_without_headers() -> None:
    with open("./mini_no_headers.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=("foo", "bar", "baz", "fee", "fii"))
        tie_count: dict[str, int] = {}
        for row in csv_reader:
            tie_name = row["baz"]
            if tie_name in tie_count:
                tie_count[tie_name] += 1
            else:
                tie_count[tie_name] = 1

my_data = [
    ["Joe", "smith", "21", "hiking"],
    ["samantha", "adams", "42", "swimming"]
]

def writing_example_csv_data() -> None:
    with open("./example.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for data in my_data:
            writer.writerow(data)


def reading_large_data_with_pandas() -> None:
    """reading a file with pandas is wicked simple, just..."""
    df = pandas.read_csv("./five_min_tie_flows.csv")
    print(df.head())


if __name__ == "__main__":
    reading_large_data_with_pandas()
