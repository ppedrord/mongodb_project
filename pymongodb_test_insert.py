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
print("Add items for the Library Database:")
def method_to_add_books_for_rent_to_the_database():
    books_for_rent = {
        "books_for_rent":   {
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
    }
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
            "book_name" : "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                            "Fantasy",
                            "Adventure"
                        ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        },
                        ]
    books_for_rent.extend(new_books_for_rent)
    collection_books_for_rent.insert_many(books_for_rent)
    return collection_books_for_rent


print(method_to_add_books_for_rent_to_the_database(),"\n")


# Add books for sale to the Library Database
print("Add books for sale to the Library Database:")
def method_to_add_books_for_sale_to_the_database():
    books_for_sale = [{
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
    }]
    new_books_for_sale = [
                            {
            "book_name" : "The Burning Bridge",
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
    books_for_sale.extend(new_books_for_sale)
    collection_books_for_sale.insert_many(books_for_sale)
    return collection_books_for_sale


print(method_to_add_books_for_sale_to_the_database(),"\n")


# Add items for sale to the Library Database
print("Add items for sale to the Library Database:")
def method_to_add_items_for_sale_to_the_database():
    items_for_sale = [{
            "item_name": "Post-it Notes",
            "color": "Jaipur Collection",
            "shape": "Square",
            "material_type": "Paper",
            "size": "14 Pads",
            "sheet_size": "3-x-3-inch",
            "item_category": "Item for Sale"
        }]
    new_items_for_sale = [
        {
            "item_name": "TICONDEROGA Pencils, Wood-Cased, Pre-Sharpened, Graphite",
            "color": "Yellow",
            "manufacturer": "Dixon Ticonderoga",
            "hardness": "HB",
            "size": "30 Count",
            "point_type": "Fine",
            "ink_color": "Black",
            "item_category": "Item for sale"
        }
    ]
    items_for_sale.extend(new_items_for_sale)
    collection_items_for_sale.insert_many(items_for_sale)
    return collection_items_for_sale


print(method_to_add_items_for_sale_to_the_database(),"\n")


def method_to_find_items_in_some_collection():



# def method_to_find_all_items_in_a_specific_category():
#
# def method_to_delete_collections():
#     collection_items_for_sale.drop()
#     collection_books_for_rent.drop()
#     collection_books_for_sale.drop()


def method_to_drop_all_collections():
    print("Dropping the Collection 'books_for_rent'...")
    collection_books_for_rent.drop()
    print("Done!\n")
    print("Dropping the Collection 'books_for_sale'...")
    collection_books_for_sale.drop()
    print("Done!\n")
    print("Dropping the Collection 'items_for_sale'...")
    collection_items_for_sale.drop()
    print("Done!")
    return collection_items_for_sale, collection_books_for_sale, collection_books_for_rent

print(method_to_drop_all_collections())



