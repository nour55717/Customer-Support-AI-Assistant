from app.rag.data_loader import CustomerSupportDataLoader
from app.rag.cleaner import DataCleaner
from app.rag.preprocessing import TextPreprocessor
from app.rag.eda import DataAnalyzer


loader = CustomerSupportDataLoader()
df = loader.load_data()

cleaner = DataCleaner()
df = cleaner.clean(df)

preprocessor = TextPreprocessor()
df = preprocessor.preprocess_dataframe(df)

analyzer = DataAnalyzer()
analyzer.analyze(df)