"""
A sample function which can be used to insert data into mongoDB synchronously.

Requirements :-
- pymongo==4.8.0
- python-dotenv==1.0.1 (being used to read data from env files.)

"""
import os
import pymongo

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

mongo_client = pymongo.MongoClient(os.getenv("MONGO_DB_URI"))
mongo_db = mongo_client["test_database"]

sample_dict_insert_mongo = {"name": "test name", "age": 25}
res = mongo_db["test_collection"].insert_one(sample_dict_insert_mongo)
print(f"The result of mongo insert operation is:  {res}")
