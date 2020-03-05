from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.json_util import loads

client = MongoClient("mongodb+srv://admin:seattleu@arch-mvj4y.azure.mongodb.net/arch?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db=client.arch
address_collecion = db.addresses

def query(query_data):
    query_data = json.loads(json.dumps(query_data))
    docs = address_collecion.find(query_data)
    return loads(dumps(docs))

def create(address):
    address = json.loads(json.dumps(address))
    address = address_collecion.insert_one(address)
    return address.inserted_id

def update(address):
    new_address = json.loads(json.dumps({'$set': address}))
    query = json.loads(json.dumps({"_id": address['id']}))
    address_collecion.update_one(query, new_address)