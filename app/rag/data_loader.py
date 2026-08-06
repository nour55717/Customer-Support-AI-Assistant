import pandas as pd
from pathlib import Path

from app.core.config import DATASET_PATH
from app.core.logger import logger


class CustomerSupportDataLoader:
    """
    Load customer support dataset from CSV file.
    """

    def __init__(self, dataset_path: Path = DATASET_PATH):
        self.dataset_path = dataset_path
        self.dataframe = None

    def load_data(self) -> pd.DataFrame:
        """
        Load CSV dataset into a pandas DataFrame.
        """

        logger.info(f"Loading dataset from: {self.dataset_path}")

        if not self.dataset_path.exists():
            logger.error(f"Dataset not found: {self.dataset_path}")
            raise FileNotFoundError(f"Dataset not found: {self.dataset_path}")

        self.dataframe = pd.read_csv(self.dataset_path)

        logger.info(f"Dataset loaded successfully.")
        logger.info(f"Rows: {self.dataframe.shape[0]}")
        logger.info(f"Columns: {self.dataframe.shape[1]}")

        return self.dataframe

    def get_dataframe(self) -> pd.DataFrame:
        """
        Return loaded dataframe.
        """

        if self.dataframe is None:
            return self.load_data()

        return self.dataframe