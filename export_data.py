import pandas as pd
import pymongo

# Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mydatabase"
COLLECTION_NAME = "customers"

def export_to_csv():
    # Connect to MongoDB
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    col = db[COLLECTION_NAME]

    print("Fetching data from MongoDB...")
    # Fetch all documents
    data = list(col.find())

    if not data:
        print("No data found to export.")
        return

    # Create DataFrame
    df = pd.DataFrame(data)

    if '_id' in df.columns:
        df = df.drop(columns=['_id'])

    # Export to CSV
    output_file = 'customers.csv'
    df.to_csv(output_file, index=False)
    print(f"Exported {len(df)} records to '{output_file}'.")

if __name__ == "__main__":
    export_to_csv()