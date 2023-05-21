from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os, pprint

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

uri = f"mongodb+srv://admin:{password}@recommend.wg2l4em.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#db connected
dbs = client.list_database_names()
test_db = client.test
#collections = test_db.list_collection_names()
#print(collections)

def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name" : "Tim",
        "type" : "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)


production_db = client.production
person_collection = production_db.person_collection

def create_documents():
    first_names = ["Tim", "Sarah", "Jeenifer"]
    last_names = ["Ruscica", "Smith", "Bart"]
    ages = ["21", "42", "15"]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name" : first_name, "last_name" : last_name, "age" : age}
        docs.append(doc)

    person_collection.insert_many(docs)

create_documents()