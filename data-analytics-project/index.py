import csv
import statistics
from pathlib import Path
import argparse

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = list(csv.reader(csvfile))[1:]
        proteins = [float(row[10]) for row in reader]
        fats = [float(row[4]) for row in reader]
        carbs = [float(row[8]) for row in reader]
        cals = [float(row[3]) for row in reader]
        data_dict = {"proteins":proteins,"fats":fats,"carbs":carbs,"cals":cals}
        total_num = len(proteins) - 1

    print("Total no. of entries:", total_num)

    return data_dict, total_num

# fats, protein, carbs, calories
def analyze_data(data_dict,size):
    print("\nAnalysis of Data:\n")

    print("Mean of proteins (in g):  ", statistics.mean(data_dict["proteins"]))
    print("Mean of fats (in g):  ", statistics.mean(data_dict["fats"]))
    print("Mean of carbs (in g):  ", statistics.mean(data_dict["carbs"]))
    print("Mean of cals (in g):  ", statistics.mean(data_dict["cals"]))
    print("")

    print("Mode of proteins (in g):  ", statistics.mode(data_dict["proteins"]))
    print("Mode of fats (in g):  ", statistics.mode(data_dict["fats"]))
    print("Mode of carbs (in g):  ", statistics.mode(data_dict["carbs"]))
    print("Mode of cals (in g):  ", statistics.mode(data_dict["cals"]))


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

    data_dict, total_num = read_csv(file_path)
    analyze_data(data_dict,total_num)
    

if __name__ == "__main__":
    main()