from pymongo import MongoClient, errors

URL = "mongodb://127.0.0.1:27017"

def main():
    try:
        with MongoClient(URL, serverSelectionTimeoutMS=3000) as client:
            client.admin.command("ping")
            print("Connected to MongoDB OK")

            db = client["eShopping"]

            users = db["users"]

            query = {"Name": "Alice Williams"}
            user = users.find_one(query)
            if user is None:
                print("No document matched:", query)
            else:
                print("Found user:", user)

    except errors.ServerSelectionTimeoutError:
        print("Cannot connect to MongoDB. Is the server running and reachable at", URL)
    except Exception as e:
        print("Unexpected error:", type(e).__name__, e)

if __name__ == "__main__":
    main()

