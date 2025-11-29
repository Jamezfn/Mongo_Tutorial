from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]

        #Delete one document
        result = coll.delete_one({"name": "Pauline"})

        #Delete many documents
        result1 = coll.delete_many({"name": "Moraa Kistar"})

        print(result.deleted_count)
        print(result1.deleted_count)
if __name__ == '__main__':
    main()