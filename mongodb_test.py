import pymongo 
import json

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Load data from JSON file
for x in mycol.find():
    print(x)