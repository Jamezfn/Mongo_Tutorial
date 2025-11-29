from typing import TypedDict
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

class Movie(TypedDict):
    names: str
    year: int

client: MongoClient = MongoClient()
db: Database[Movie] = client["test_database"]

collection: Collection[Movie] = db.create_collection("tests")

print("Databases:", client.list_database_names())
print("Collections in test_database:", db.list_collection_names())
