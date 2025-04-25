"""Reading a writing CSV files refresher.

An overview of the options for reading/writing CSV files
using the std lib csv files or pandas.
"""

# Using the standard library csv package

import csv

with open("./five_min_tie_flows.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    tie_count: dict[str, int] = {}
    for row in csv_reader:
        tie_name = row["tie_flow_name"]
        if tie_name in tie_count:
            tie_count[tie_name] += 1
        else:
            tie_count[tie_name] = 1
    print(tie_count)