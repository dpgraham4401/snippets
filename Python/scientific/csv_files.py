"""Reading a writing CSV files refresher.

An overview of the options for reading/writing CSV files
using the std lib csv files or pandas.
"""

# Using the standard library csv package

import csv

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


if __name__ == "__main__":
    read_mini_without_headers()
