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
        nrows=500,
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

    print("\nSummary Statistics:")
    stats = {}
    stats["Rating"] = df["Rating"].describe()
    for col in ["Type", "BodyPart", "Equipment", "Level"]:
        stats[col] = df[col].value_counts(normalize=True) * 100
    print("Numerical Summary:")
    print(stats["Rating"])
    print("\nCategorical Summaries (in percentages):")
    for col in ["Type", "BodyPart", "Equipment", "Level"]:
        print("\n")
        print(stats[col])


def handle_missing_values(df):
    df = df.copy()
    print("\n\nBefore handling missing values:")
    print(df.isnull().sum())
    df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
    print("\nAfter handling missing values:")
    print(df.isnull().sum())

    return df


def remove_duplicates(df):
    columns_to_consider = df.columns[1:]
    distinct = df.drop_duplicates(subset=columns_to_consider, keep="first")

    num_duplicates_removed = len(df) - len(distinct)
    nCols = len(distinct.columns)
    nRows = len(distinct)

    print(f"\n\nNumber of duplicates removed: {num_duplicates_removed}")
    print(f"No. of columns after removing duplicates: {nCols}")
    print(f"No. of rows after removing duplicates: {nRows}")

    return distinct


def feature_engineering(df):
    df = df.copy()

    df["Type_BodyPart"] = df["Type"] + "_" + df["BodyPart"]

    df["Title_word_count"] = df["Title"].str.split().str.len()

    df["Rating_category"] = pd.cut(
        df["Rating"],
        bins=[0, 2, 4, 6, 8, 10],
        labels=["Very Low", "Low", "Medium", "High", "Very High"],
        include_lowest=True,
    )

    level_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
    df["Level_numeric"] = df["Level"].map(level_map)
    df["Difficulty_score"] = df["Level_numeric"] * df["Rating"]

    return df


# def visualize_data(df):
#     # Create visualizations to better understand the data


def main():
    data_frame = load_data("megaGymDataset.csv")
    explore_data(data_frame)
    distinct_df = remove_duplicates(data_frame)
    cleaned = handle_missing_values(distinct_df)
    engineered = feature_engineering(cleaned)
    print(engineered)


if __name__ == "__main__":
    main()
