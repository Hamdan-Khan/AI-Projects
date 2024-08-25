import csv
import statistics
from pathlib import Path
import argparse

def read_csv(filename):
    columns_to_keep = {'food', 'Protein', 'Caloric Value', 'Fat', 'Carbohydrates'}

    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        data_list = list(csvreader)
        filtered = []
        for row in data_list:
            filtered_row = {k: v for k, v in row.items() if any(k.startswith(prefix) for prefix in columns_to_keep)}
            filtered.append(filtered_row)
        total_num = len(data_list) - 1

    print("Total no. of entries:", total_num)

    n = int(input("Enter the number of entries you want to see: "))
    
    if n < 1 or n > total_num:
        print("Out of range")
    else:
        print(f'\nFirst {n} rows are:\n')
        for data in filtered[:n]:
            print(data)

    return filtered, total_num

# fats, protein, carbs, calories
def analyze_data(data_list,size):
    print("\n\n\n Analysis of Data:   \n\n\n")
    sums = {"calories":0,"protein":0,"carbs":0,"fats":0}
    for data in data_list[:5]:
        sums["protein"] += float(data["Protein"])
        sums["calories"] += float(data["Caloric Value"])
        sums["fats"] += float(data["Fat"])
        sums["carbs"] += float(data["Carbohydrates"])
    print("Sums: ",sums)
    


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

    data_list, total_num = read_csv(file_path)
    analyze_data(data_list,total_num)
    

if __name__ == "__main__":
    main()