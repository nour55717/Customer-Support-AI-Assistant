import pandas as pd

from app.core.logger import logger


class DataAnalyzer:
    """
    Perform exploratory data analysis.
    """

    def analyze(self, df: pd.DataFrame):
        logger.info("Dataset Analysis")

        print("\n========== DATASET INFO ==========")
        print(df.info())

        print("\n========== FIRST 5 ROWS ==========")
        print(df.head())

        print("\n========== MISSING VALUES ==========")
        print(df.isnull().sum())

        print("\n========== DUPLICATES ==========")
        print(df.duplicated().sum())

        print("\n========== CATEGORY COUNTS ==========")
        print(df["category"].value_counts())

        print("\n========== INTENT COUNTS ==========")
        print(df["intent"].value_counts())

        print("\n========== DATASET SHAPE ==========")
        print(df.shape)