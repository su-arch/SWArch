# this is used to test insertion and find ops in MongoDB
# you can ignore me

from pymongo import MongoClient
from random import randint

# connect to server
# Note: before you use the db named testdb, you should create it beforehand in 
# MongoDB shell
# for local mongodb
# client = MongoClient("127.0.0.1:27017")
# for remote mongodb
client = MongoClient("mongodb+srv://admin:seattleu@arch-mvj4y.azure.mongodb.net/testdb?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
testdb=client.testdb

print (testdb)

name = ['acity', 'bcity', 'ccity', 'dcity', 'ecity']
address = ['add1', 'add2', 'add3', 'add4', 'add5', 'add6', 'add7', 'add8']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# create 100 documents and put them into the collection named "cities"
# Note: don't run this part more than 2 times Or your database will be very large
for i in range(1, 100):
    city = {
        'name': name[randint(0, len(name) - 1)],
        'address': address[randint(0, len(address) - 1)],
        'number': number[randint(0, len(number) - 1)]
    }
    testdb.cities.insert_one(city)
    print (city)

# search documents whose name is 'acity' and address is 'add1'
my_query = {'name': 'acity', 'address': 'add1'}
my_docs = testdb.cities.find(my_query)
for x in my_docs:
    print (x)