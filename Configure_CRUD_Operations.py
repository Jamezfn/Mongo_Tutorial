from pymongo import MongoClient, ReadPreference, WriteConcern
from pymongo.read_concern import ReadConcern

URL = "mongodb://127.0.0.1:27017"

def main():
    with MongoClient(URL) as client:
        db = client.get_database(
            "test-database",
            read_preference=ReadPreference.SECONDARY,
            read_concern=ReadConcern("local"),
            write_concern=WriteConcern(w="majority")
        )

        print(db.name)
        print(db.read_concern)
        print(db.write_concern)

        coll = db.get_collection(
            "tests",
            read_preference=ReadPreference.SECONDARY,
            read_concern=ReadConcern("local"),
            write_concern=WriteConcern(w="majority")
        )

        print(coll.name)
        print(coll.read_concern)
        print(coll.write_concern)

if __name__ == "__main__":
    main()
