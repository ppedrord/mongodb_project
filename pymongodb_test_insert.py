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
print("Add books in the Library Database:")
def method_to_add_items_to_the_database(new_books_for_rent: list = None, new_books_for_sale: list = None,
                                                 new_items_for_sale: list = None) -> tuple:
    """
    :param new_books_for_rent: Add new books for rent to the library database
    :param new_books_for_sale: Add new books for sale to the library database
    :param new_items_for_sale: Add new items for sale to the library database
    :return: An update in the collections that were modified
    """

    all_items_in_library = {
        "books":   [{
                        "books_for_rent": [
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
                                          ],
                        "books_for_sale": [
                                            {
        "_id": "BFS0001",
        "book_name": "The Ruins of Gorlan",
        "author": "John Flanagan",
        "year": "2004",
        "price": 30.00,
        "category": [
            "Fantasy",
            "Adventure"
        ],
        "series": "Ranger's Apprentice",
        "item_category": "Book for sale"
    }
                                          ]
        }],
        "items": [{
                        "items_for_sale": [{
            "_id": "IFS0001",
            "item_name": "Post-it Notes",
            "price": 5.99,
            "color": "Jaipur Collection",
            "shape": "Square",
            "material_type": "Paper",
            "size": "14 Pads",
            "sheet_size": "3-x-3-inch",
            "item_category": "Item for Sale"
        }]
        }]
    }


    if new_books_for_rent:
        all_items_in_library["books"][0]["books_for_rent"].extend(new_books_for_rent)
        collection_books_for_rent.insert_many(all_items_in_library["books"][0]["books_for_rent"])

    if new_books_for_sale:
        all_items_in_library["books"][0]["books_for_sale"].extend(new_books_for_sale)
        collection_books_for_sale.insert_many(all_items_in_library["books"][0]["books_for_sale"])

    if new_items_for_sale:
        all_items_in_library["items"][0]["items_for_sale"].extend(new_items_for_sale)
        collection_items_for_sale.insert_many(all_items_in_library["items"][0]["items_for_sale"])

    return collection_books_for_rent, collection_books_for_sale, collection_items_for_sale


print(method_to_add_items_to_the_database(), "\n")




