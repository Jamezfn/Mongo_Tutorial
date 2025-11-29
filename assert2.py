from typing import TypedDict
from pymongo import MongoClient
from pymongo.collection import Collection
class Movie(TypedDict):
    name: str
    year: int

client: MongoClient = MongoClient()
collection: Collection[Movie] = client["test_database"]["tests"]
inserted = collection.insert_one(Movie(name="Jurassic Park", year=1993))
result = collection.find_one({"name": "Jurassic Park"})
# _id is present but was added by PyMongo; this will raise a type-checking error
assert result is not None
assert result["_id"]
