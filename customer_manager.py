import pymongo

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def main():
    while True:
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Update Customer")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_customer()
        if choice == '2':
            view_customers()
        elif choice == '3':
            delete_customer()
        elif choice == '4':
            update_customer()
        elif choice == '5': 
            break

def add_customer():
    name = input("Enter customer name: ")
    nickname = input("Enter customer nickname: ")
    address = input("Enter customer address: ")
    customer = {"name": name, "nickname": nickname, "address": address}
    mycol.insert_one(customer)
    print("Customer added successfully.")

def view_customers():
    for x in mycol.find():
        # Use .get() to avoid errors if a field is missing
        print(f"{x.get('name', 'N/A'):<10} | {x.get('nickname', 'N/A'):<10} | {x.get('address', 'N/A')}")

def update_customer():
    name = input("Enter the name of the customer to update: ")
    new_nickname = input("Enter nickname: ")
    new_address = input("Enter new address: ")
    mycol.update_one({"name": name}, {"$set": {"nickname": new_nickname, "address": new_address}})
    print("Customer info updated.")
    
def delete_customer():
    name = input("Enter the name of the customer to delete: ")
    if mycol.find_one({"name": name}):
        mycol.delete_one({"name": name})
        print("Customer deleted.")
    else:
        print("Customer not found.")

if __name__ == "__main__":
    main()