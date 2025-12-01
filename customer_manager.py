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

def add_customer():
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    customer = {"name": name, "address": address}
    mycol.insert_one(customer)
    print("Customer added successfully.")

def view_customers():
    for x in mycol.find():
        print(f"{x['name']:<10} | {x['address']}")

def update_customer():
    name = input("Enter the name of the customer to update: ")
    new_address = input("Enter new address: ")
    mycol.update_one({"name": name}, {"$set": {"address": new_address}})
    print("Customer info updated.")
    
def delete_customer():
    name = input("Enter the name of the customer to delete: ")
    mycol.delete_one({"name": name})
    print("Customer deleted.")

if __name__ == "__main__":
    main()