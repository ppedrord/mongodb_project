def get_database():
    from pymongo import MongoClient
    import pymongo

    # Use the atlas url to connect pyhton to MongoDB using pymong
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(connection_string)
    return client['library_database']

# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#
dbname = get_database()

collection_books_for_rent = dbname["books_for_rent"]
collection_books_for_sale = dbname["books_for_sale"]
collection_items_for_sale = dbname["items_for_sale"]

# Add items for the Library Database

books_for_rent = [
                    {
            "_id": "U1IT0000001",
            "book_name": "The Road to Serfdom",
            "author": "Friedrich A. Hayek",
            "year": "1944",
            "price": 2.99,
            "category": [
                            "Political Science",
                            "Economics"
                        ],
            "item_category": "Book for rent"
        },
                    {
            "_id": "U1IT0000002",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 3.49,
            "category": [
                            "Political Science"
                        ],
            "item_category": "Book for rent"
        }
                ]
new_books_for_rent = [
                            {
            "_id": "U1IT0000003",
            "book_name": "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for Sale"
        },
                            {
            "_id": "U1IT0000004",
            "book_name" : "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                            "Fantasy",
                            "Adventure"
                        ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for Rent"
        },
                        ]
books_for_rent.extend(new_books_for_rent)
collection_books_for_rent.insert_many(books_for_rent)


# Add item without an _id
book_3 = {
            "book_name" : "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 30.00,
            "category": [
                            "Fantasy",
                            "Adventure"
                        ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for Sale"
        }
collection_books_for_sale.insert_one(book_3)

item_1 = {
            "item_name": "Post-it Notes",
            "color": "Jaipur Collection",
            "shape": "Square",
            "material_type": "Paper",
            "size": "14 Pads",
            "sheet_size": "3-x-3-inch",
            "item_category": "Item for Sale"
        }
collection_items_for_sale.insert_one(item_1)

#