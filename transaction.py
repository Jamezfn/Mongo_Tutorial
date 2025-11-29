from pymongo import MongoClient, WriteConcern
from pymongo.read_concern import ReadConcern
from pymongo.errors import ConnectionFailure, OperationFailure

URL = 'mongodb+srv://jamesmakachia19_db_user:cuRXhzxrNQ9cgR5a@cluster0.cs55y0o.mongodb.net/?appName=Cluster0'

client = MongoClient(URL)

transaction_db = client['transaction_db']
transaction_db.create_collection('transaction_collection')

transaction_collection = transaction_db['transaction_collection']

def insert_transaction(session):
    transaction_collection.with_options(
        write_concern=WriteConcern(w="majority"),
        read_concern=ReadConcern(level="majority")
        )

    transaction_collection.insert_one(
        {"name": "John", "age": 30}, 
        session=session
        )
    
    transaction_collection.insert_one(
        {"name": "Jane", "age": 25}, 
        session=session
        )

with client.start_session() as session:
    session.start_transaction()
    try:
        insert_transaction(session)
        session.commit_transaction()
        print("Transaction succeeded")
    except (ConnectionFailure, OperationFailure) as e:
        print(f"Transaction failed: {e}")

client.close()
        
