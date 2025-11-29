from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]

        result = coll.estimated_document_count()
        print(result)

        result2 = coll.count_documents({})
        print(result2)

if __name__ == '__main__':
    main()