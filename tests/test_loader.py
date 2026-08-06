from app.rag.data_loader import CustomerSupportDataLoader

loader = CustomerSupportDataLoader()

df = loader.load_data()

print(df.head())

print(f"\nRows: {len(df)}")
print(f"Columns: {len(df.columns)}")