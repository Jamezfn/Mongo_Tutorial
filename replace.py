from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]
        result = coll.replace_one({"name": "James"}, {"name": "Pauline"})
        print(result.modified_count)
if __name__ == '__main__':
    main()
