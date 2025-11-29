from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]
        
        #Update One
        query_filter = {
                "name": "Kistar Moraa"
                }

        update_op = {
                "$set": {
                    "name": "Moraa Kistar"
                    }
                }

        result = coll.update_one(query_filter, update_op)

        #Update Many

        query_filter1 = {
                "name": "Kistar Moraa"
                }

        update_op1 = {
                "$set": {
                    "name": "Moraa1 Kistar1"
                    }
                }

        result1 = coll.update_one(query_filter1, update_op1)

        print(result.modified_count)
        print(result1.modified_count)

if __name__ == '__main__':
    main()
