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


# def create_static_visualizations(df : pd.DataFrame):
#     sns.set_style("darkgrid")


# def create_interactive_visualizations(df):
#     # Create interactive visualizations using Plotly


def main():
    df = load_data("2019.csv")
    df = preprocess_data(df)


if __name__ == "__main__":
    main()
