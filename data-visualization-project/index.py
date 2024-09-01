import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


def load_data(file_path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    print(df.dtypes)
    print(df.isnull().sum())
    return df


def create_static_visualizations(df: pd.DataFrame):
    sns.set_style("dark")

    plt.figure(figsize=(10, 6))
    sns.histplot(df["Score"], kde=True)
    plt.title("Distribution of Score")
    plt.xlabel("Score")
    plt.ylabel("Count")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=df["Country"][:15], y=df["Generosity"][:15])
    plt.title("Country vs. Generosity")
    plt.xlabel("Country")
    plt.ylabel("Generosity")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# def create_interactive_visualizations(df):
#     # Create interactive visualizations using Plotly


def main():
    df = load_data("2019.csv")
    df = preprocess_data(df)
    create_static_visualizations(df)


if __name__ == "__main__":
    main()
