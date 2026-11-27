"""Read an outage's error log CSV. The summary logic comes in the next task."""
import csv
import sys


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python summarize.py data/<outage>.csv")
    rows = read_rows(sys.argv[1])
    print(f"read {len(rows)} rows")
