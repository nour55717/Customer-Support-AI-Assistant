import pandas as pd

from app.core.logger import logger


class DataCleaner:
    """
    Clean customer support dataset.
    """

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Cleaning dataset...")

        df = df.copy()

        # Remove duplicate rows
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)

        logger.info(f"Removed {before - after} duplicate rows.")

        # Remove rows with missing instruction/response
        df = df.dropna(subset=["instruction", "response"])

        # Reset index
        df = df.reset_index(drop=True)

        logger.info(f"Dataset shape after cleaning: {df.shape}")

        return df