from pathlib import Path
from dotenv import load_dotenv
import os


# ==========================================
# Project Root
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[2]


# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv(BASE_DIR / ".env")


# ==========================================
# Project Paths
# ==========================================

DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "customer_support.csv"

CHROMA_DB_PATH = BASE_DIR / "chroma_db"

LOG_DIR = BASE_DIR / "logs"


# ==========================================
# Embedding Model
# ==========================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


# ==========================================
# Retrieval Settings
# ==========================================

TOP_K = 5


# ==========================================
# OpenAI
# ==========================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# ==========================================
# Application Settings
# ==========================================

APP_NAME = "Customer Support AI"

VERSION = "1.0.0"

DEBUG = True