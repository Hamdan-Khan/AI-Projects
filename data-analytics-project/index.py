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
        names = [row[2] for row in reader]
        data_dict = {"proteins":proteins,"fats":fats,"carbs":carbs,"cals":cals,"names":names}
        total_num = len(proteins) - 1

    print("Total no. of entries:", total_num)

    return data_dict, total_num

# fats, protein, carbs, calories
def analyze_data(data_dict,size):
    print("\nAnalysis of Data:\n")

    nutrients = ["proteins", "fats", "carbs", "cals"]
    stats = ["mean", "mode", "median", "stdev"]
    
    results = {stat: [] for stat in stats}

    for nutrient in nutrients:
        # sum/n
        results["mean"].append(statistics.mean(data_dict[nutrient]))
        # most repeated val
        results["mode"].append(statistics.mode(data_dict[nutrient]))
        # mid point of data
        results["median"].append(statistics.median(data_dict[nutrient]))
        # [(xi - mean)^2 / n-1]^1/2
        results["stdev"].append(statistics.stdev(data_dict[nutrient]))

    for stat in stats:
        print(f"\n{stat.capitalize()}:")
        for i, nutrient in enumerate(nutrients):
            print(f"{nutrient.capitalize()} (in g): {results[stat][i]:.2f}")

    return results




def filter_data(data, column, value):
    print(f"\nFiltering by column: {column}, value: {value}\n")
    if value in data[column]:
        i = data[column].index(value)
        print(f"Nutrients of {data["names"][i]}")
        print("\n".join(f"{key} : {data[key][i]} gm" for key in data.keys() if key != "names"))

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
    results = analyze_data(data_dict,total_num)

    if args.filter:
        filter_column, filter_value = args.filter
        filter_data(data_dict,filter_column,filter_value) 

if __name__ == "__main__":
    main()