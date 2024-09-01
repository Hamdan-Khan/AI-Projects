import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    return df


# def preprocess_data(df):
#     # Handle missing values, data types, etc.
#     return df

# def create_static_visualizations(df):
#     # Create various static visualizations using Matplotlib and Seaborn

# def create_interactive_visualizations(df):
#     # Create interactive visualizations using Plotly


def main():
    df = load_data("world_happiness_report.csv")


if __name__ == "__main__":
    main()
