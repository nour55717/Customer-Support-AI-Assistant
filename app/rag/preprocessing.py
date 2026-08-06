import re
import pandas as pd

from app.core.logger import logger


class TextPreprocessor:
    """
    Preprocess customer support text.
    """

    def clean_text(self, text: str) -> str:
        if pd.isna(text):
            return ""

        text = str(text).lower()
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text

    def preprocess_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Preprocessing dataset...")

        df = df.copy()

        df["instruction"] = df["instruction"].apply(self.clean_text)
        df["response"] = df["response"].apply(self.clean_text)

        logger.info("Preprocessing completed.")

        return df