from fastapi import FastAPI
import pymongo 
from pydantic import BaseModel

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

app = FastAPI()

# Define the data model for a Customer
class Customer(BaseModel):
    name: str
    nickname: str = ""  
    address: str

#  "@app.get" tells FastAPI that this function handles GET requests to the URL "/"
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/customers/")
async def get_customers():
    customers = []
    for x in mycol.find():
        customers.append({
            "name": x.get("name", ""),
            "nickname": x.get("nickname", ""),
            "address": x.get("address", "")
        })
    return customers

@app.post("/customers/")
async def create_customer(customer: Customer):
    # Convert the Pydantic model to a dictionary
    customer_dict = customer.dict()
    
    # Insert into MongoDB
    result = mycol.insert_one(customer_dict)
    
    return {"message": "Customer added", "id": str(result.inserted_id)}

@app.get("/customers/{name}")
async def get_customer(name: str):
    customer = mycol.find_one({"name": name})
    if customer:
        return {
            "name": customer.get("name", ""),
            "nickname": customer.get("nickname", ""),
            "address": customer.get("address", "")
        }
    return {"error": "Customer not found"}

@app.delete("/customers/{name}")
async def delete_customer(name: str):
    result = mycol.delete_one({"name": name})
    if result.deleted_count:
        return {"message": "Customer deleted"}
    return {"error": "Customer not found"}