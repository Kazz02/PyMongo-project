import pymongo

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def main():
    while True:
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '2':
            view_customers()
        elif choice == '4':
         break

def view_customers():
    for x in mycol.find():
        print(f"{x['name']:<10} | {x['address']}")
    
if __name__ == "__main__":
    main()