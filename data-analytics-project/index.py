import csv
import statistics
from pathlib import Path
import argparse

fields = []
rows = []

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields.append(next(csvreader))

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

# def analyze_data(data):
#     # Perform statistical analysis

# def filter_data(data, column, value):
#     # Filter data based on column and value

# def generate_report(analysis_results):
#     # Generate and print a summary report

def main():
    parser = argparse.ArgumentParser(description="Sales Data Analyzer")
    parser.add_argument("file_path", help="Enter path to csv file")
    parser.add_argument("--filter", nargs=2, metavar=("COLUMN", "VALUE"), help="Filter data")
    args = parser.parse_args()

    file_path = Path(args.file_path)

    if not file_path.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    read_csv(file_path)
    

if __name__ == "__main__":
    main()