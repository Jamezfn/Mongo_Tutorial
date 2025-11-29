from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]

        #Insert One
        result = coll.insert_one({"name": "Kistar Moraa"})

        #Insert Many
        doc_list = [
                {"name": "Pauline"},
                {"name": "Dalot"},
                {"name": "Bruno"}
                ]
        result2 = coll.insert_many(doc_list)

        print(result.acknowledged)
        print(result2.acknowledged)

if __name__ == '__main__':
    main()
