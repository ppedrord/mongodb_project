def get_database():
    from pymongo import MongoClient
    import pymongo

    # Use the atlas url to connect pyhton to MongoDB using pymong
    connection_string = "mongodb+srv://ppedrord:deyvershow@library-test.xja33.mongodb.net/Library-TEST?retryWrites=true&w=majority"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(connection_string)
    return client['user_library_list']

# # This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    dbname = get_database()

collection_name = dbname["user_1_books"]

# Add items for the Library Database
book_1 = {
            "_id": "U1IT00001",
            "book_name": "The Road to Serfdom",
            "author": "Friedrich A. Hayek",
            "year": "1944",
            "price": 4.99,
            "category": [
                            "Political Science",
                            "Economics"
                        ]
        }

book_2 = {
            "_id": "U1IT00002",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 5.99,
            "category": [
                            "Political Science",
                        ]
        }
collection_name.insert_many([book_1, book_2])


# Add item without an _id
book_3 = {
            "book_name" : "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2008",
            "price": 30.00,
            "category": [
                            "Political Science",
                        ],
            "series": "Ranger's Apprentice",
        }
collection_name.insert_one(book_3)
