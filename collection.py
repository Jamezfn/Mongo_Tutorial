from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]
        db.create_collection("kistar-d")

        # Time Series Collection
        db.create_collection("james-d", timeseries={"timeField": "timestamp"})

        # Capped Collection
        db.create_collection("moraa", capped=True, size=1000)

        # Get a List of Collections
        print("Databases:", client.list_database_names())
        print("Collections in eShopping:", db.list_collection_names())
        

if __name__ == '__main__':
    main()
