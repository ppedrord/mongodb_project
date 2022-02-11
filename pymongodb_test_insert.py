import json

# Open JSON file
open_json = open("all_items_in_library.json")

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

# Return JSON object as a dictionary
all_items_in_library = json.load(open_json)
print(all_items_in_library)


# Add items for the Library Database
print("Add books in the Library Database:")
def method_to_add_items_to_the_database(new_books_for_rent: list = None, new_books_for_sale: list = None,
                                                 new_items_for_sale: list = None) -> dict:
    """ Method to add items to the Library Database
    :param new_books_for_rent: Add new books for rent to the library database
    :param new_books_for_sale: Add new books for sale to the library database
    :param new_items_for_sale: Add new items for sale to the library database
    :return: An update in the collections that were modified
    """

    if new_books_for_rent:
        all_items_in_library["books"][0]["books_for_rent"].extend(new_books_for_rent)
        collection_books_for_rent.insert_many(all_items_in_library["books"][0]["books_for_rent"])

    if new_books_for_sale:
        all_items_in_library["books"][0]["books_for_sale"].extend(new_books_for_sale)
        collection_books_for_sale.insert_many(all_items_in_library["books"][0]["books_for_sale"])

    if new_items_for_sale:
        all_items_in_library["items"][0]["items_for_sale"].extend(new_items_for_sale)
        collection_items_for_sale.insert_many(all_items_in_library["items"][0]["items_for_sale"])

    return all_items_in_library


def method_to_find_items_in_the_database(item_search: str) -> list:
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




