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


# def explore_data(df):
#     # Display basic information about the dataset
#     # Show summary statistics

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
    load_data("megaGymDataset.csv")


if __name__ == "__main__":
    main()
