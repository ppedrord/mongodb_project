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

all_items_in_library = {
  "books": [
    {
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
    }
  ],
  "items": [
    {
      "items_for_sale": [
        {
          "_id": "IFS0001",
          "item_name": "Post-it Notes",
          "price": 5.99,
          "color": "Jaipur Collection",
          "shape": "Square",
          "material_type": "Paper",
          "size": "14 Pads",
          "sheet_size": "3-x-3-inch",
          "item_category": "Item for Sale"
        }
      ]
    }
  ]
}

# Add items for the Library Database
def method_to_add_items_to_the_database(new_books_for_rent: list = None, new_books_for_sale: list = None,
                                                 new_items_for_sale: list = None) -> dict:
    """ Method to add items to the Library Database
    :param new_books_for_rent: Add new books for rent to the library database
    :param new_books_for_sale: Add new books for sale to the library database
    :param new_items_for_sale: Add new items for sale to the library database
    :return: An update in the collections that were modified
    """

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
            "item_category": "Book for rent"
        },
        {
            "_id": "U1IT0000004",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        }
    ]
    new_books_for_sale = [
        {
            "_id": "BFS0002",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for sale"
        },
        {
            "_id": "BFS0003",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 34.99,
            "category": [
                "Political Science"
            ],
            "item_category": "Book for sale"
        }
    ]
    new_items_for_sale = [
        {
            "_id": "IFS0002",
            "item_name": "TICONDEROGA Pencils, Wood-Cased, Pre-Sharpened, Graphite",
            "price": 5.99,
            "color": "Yellow",
            "manufacturer": "Dixon Ticonderoga",
            "hardness": "HB",
            "size": "30 Count",
            "point_type": "Fine",
            "ink_color": "Black",
            "item_category": "Item for sale"
        }
    ]

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

print(method_to_add_items_to_the_database())



def find_many(item_search: str) -> list:
    """
    A method to find items in the database using their names
    :param item_search: The name of the item to be found
    :return: A list containing all items with the same name in the database
    """
    list_result_item_search = []
    query_book_name = {"book_name": item_search}
    query_item_name = {"item_name": item_search}

    result_book_for_rent_search = collection_books_for_rent.find_one(query_book_name)
    if result_book_for_rent_search is not None:
        list_result_item_search.append(result_book_for_rent_search)

    result_book_for_sale_search = collection_books_for_sale.find_one(query_book_name)
    if result_book_for_sale_search is not None:
        list_result_item_search.append(result_book_for_sale_search)

    result_item_for_sale_search = collection_items_for_sale.find_one(query_item_name)
    if result_item_for_sale_search is not None:
        list_result_item_search.append(result_item_for_sale_search)

    return list_result_item_search

print(method_to_find_items_in_the_database(item_search))
