from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.json_util import loads
from bson.objectid import ObjectId  


client = MongoClient("mongodb+srv://admin:seattleu@arch-mvj4y.azure.mongodb.net/arch?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db=client.arch
address_collecion = db.addresses


def query_by_id(id):
    """
    find one document by id, which is the _id field in the database
    param [id]: str
    return: one document at most in the json format;
            if such data doesn't exist, None will be returned
    
    eg: id = '5e6688afd64550c9d16a36c6'
    it wil return this one document with the same value in the _id field
    """
    query_data = {'_id': ObjectId(str(id))}
    result = _query(query_data)
    if len(result) == 0:
        return None
    else:
        return result[0]


def query(query_data):
    """
    query documents by query_data
    param [query_data]: dict
    return: a list of documents and each document is a dict;
            if not exist, the returned list length will be 0

    eg: query_data = {'country': 'America', 'street1': 'blabla...'}
        it will return all the documents which has 'America' value in the 'country' field
        and 'blabla...' value in the 'street1' field.
    """
    return _query(query_data)


def query_by_country_name(name):
    """
    find documents by country name, which is the 'country' field in the database
    param [name]: str
    return: a list of documents and each document is a dict
            if not exist, the returned list length will be 0
    
    eg: name = 'CHILE'
        it wil return these documents with the same value in the country field
    """
    query_data = {'country': name}
    result = _query(query_data)
    return result


def _query(query_data):
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

