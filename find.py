from pymongo import MongoClient

URL = "mongodb://127.0.0.1:27017"

def main():
    """Databases and Collections"""
    with MongoClient(URL) as client:
        db = client["test_database"]

        coll = db["tests"]

        #Find one document
        result = coll.find_one({"name": "Dalot"})

        #Find Multiple
        result2 = coll.find({"name": "James"})
        for doc in result2:
            print(doc)

        #Find all
        result3 = coll.find({})
        for doc in result3:
            print(doc)

        #Find with projection
        result4 = coll.find({}, {"name": 1, "_id": 0})
        for doc in result4:
            print(doc)

        #Find with sort
        result5 = coll.find().sort("name", 1)
        for doc in result5:
            print(doc)

        #Find with limit
        result6 = coll.find().limit(2)
        for doc in result6:
            print(doc)

        #Find with skip
        result7 = coll.find().skip(1)
        for doc in result7:
            print(doc)


        print(f"Find one: {result}")

if __name__ == '__main__':
    main()