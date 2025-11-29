from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Deleting a collection"""
    with MongoClient(URL) as client:
        #Delete a collection
        db = client["test_database"]
        db["moraa"].drop()

        #Delete a Database
        client.drop_database("test_database")

if __name__ == '__main__':
    main()
