from fastapi import FastAPI
import pymongo 

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


app = FastAPI()

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