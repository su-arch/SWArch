# this is used to test insertion and find ops in MongoDB
# you can ignore me

from pymongo import MongoClient
from random import randint

# connect to server
# Note: before you use the db named testdb, you should create it beforehand in 
# MongoDB shell
client = MongoClient("127.0.0.1:27017")
testdb=client.testdb

name = ['acity', 'bcity', 'ccity', 'dcity', 'ecity']
address = ['add1', 'add2', 'add3', 'add4', 'add5', 'add6', 'add7', 'add8']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# create 1000,000 documents and put them into the collection named "cities"
# Note: don't run this part more than 2 times Or your database will be very large
for i in range(1, 1000000):
    city = {
        'name': name[randint(0, len(name) - 1)],
        'address': address[randint(0, len(address) - 1)],
        'number': number[randint(0, len(number) - 1)]
    }
    testdb.cities.insert_one(city)

# search documents whose name is 'acity' and address is 'add1'
my_query = {'name': 'acity', 'address': 'add1'}
my_docs = testdb.cities.find(my_query)
for x in my_docs:
    print (x)