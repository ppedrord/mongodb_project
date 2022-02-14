from pymongo import MongoClient


def get_client():
    # Use the atlas url to connect pyhton to MongoDB using pymong
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9"

    # Create a connection using MongoClient
    client = MongoClient(connection_string)
    return client['library']





