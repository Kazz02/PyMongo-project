import pymongo
from faker import Faker

# Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mydatabase"
COLLECTION_NAME = "customers"

def seed_database(count):
    # Connect to MongoDB
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    col = db[COLLECTION_NAME]
    
    # Initialize Faker
    fake = Faker()
    
    print(f"Generating {count} fake customers...")
    
    customers = []
    for _ in range(count):
        customer = {
            "name": fake.name(),
            "nickname": fake.user_name(),
            "address": fake.address().replace('\n', ', ')
        }
        customers.append(customer)
    
    # Insert all at once (more efficient)
    if customers:
        col.insert_many(customers)
        print(f"Successfully added {count} customers to the database!")

if __name__ == "__main__":
    try:
        num = int(input("How many fake customers do you want to generate? "))
        seed_database(num)
    except ValueError:
        print("Please enter a valid number.")
