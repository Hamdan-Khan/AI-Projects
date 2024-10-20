import nltk
import os

nltk.data.path.append("\\tmp")


def download_nltk_data():
    if not os.path.exists("\\tmp/nltk_data"):
        nltk.download("punkt", download_dir="\\tmp")
        nltk.download("stopwords", download_dir="\\tmp")
        nltk.download("punkt_tab", download_dir="\\tmp")


def main():
    download_nltk_data()


if __name__ == "__main__":
    main()
