import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    data = pd.read_csv(
        file_path,
        usecols=[
            "Unnamed: 0",
            "Title",
            "Type",
            "BodyPart",
            "Equipment",
            "Level",
            "Rating",
        ],
        nrows=1000,
    )
    return data


def explore_data(df):
    if df.empty:
        print("Data missing.")
        return
    nCols = len(df.columns)
    nRows = int(df.size / nCols)
    print(f"No. of columns: {nCols}")
    print(f"No. of rows: {nRows}")
    print("\nData Sample:")
    print(df[:10])
    print("\nData Types:")
    print(df.dtypes)
    # Show summary statistics


# def handle_missing_values(df):
#     # Identify and handle missing values

# def convert_data_types(df):
#     # Convert data types if necessary

# def remove_duplicates(df):
#     # Check for and remove duplicate entries

# def feature_engineering(df):
#     # Create new features or transform existing ones

# def visualize_data(df):
#     # Create visualizations to better understand the data


def main():
    data_frame = load_data("megaGymDataset.csv")
    explore_data(data_frame)


if __name__ == "__main__":
    main()
