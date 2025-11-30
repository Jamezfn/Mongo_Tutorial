from pymongo import MongoClient
from gridfs import GridFSBucket
from bson.objectid import ObjectId

URL = "mongodb://127.0.0.1:27017"

def main():
    with MongoClient(URL) as client:
        db = client["test_database"]
        bucket = GridFSBucket(db)
        with bucket.open_upload_stream("test_file.txt", metadata={"contentType": "text/plain"}) as upload_stream:
            upload_stream.write(b"Hello, world!")

        for file in bucket.find():
            print(
                f"filename: {file.filename}, "
                f"id: {file._id}, "
                f"length: {file.length} bytes, "
                f"upload_date: {file.upload_date}, "
                f"contentType: {file.metadata.get('contentType') if file.metadata else None}"
            )

        file = bucket.open_download_stream(ObjectId("692b82a929cd180603ab5339"))
        contents = file.read()
        print(contents.decode("utf-8"))

        # Rename
        bucket.rename(ObjectId("692b82a929cd180603ab5339"), "Hello.txt")

        # Delete
        bucket.delete(ObjectId("692b83ff15c02f2f9330ca5a"))
        bucket.delete(ObjectId("692b841b797e8531ea185e94"))
        bucket.delete(ObjectId("692b84c8e812cfc1ce500945"))
        bucket.delete(ObjectId("692b854e83c6bb41e40efc19"))

if __name__ == "__main__":
    main()
