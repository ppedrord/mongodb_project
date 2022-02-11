from pymongodb_basic import all_items_in_library, collection_books_for_rent


new_book_for_rent = [{
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
    }]
new_books_for_rent = [
    {
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
def create_one(new_book_for_rent: dict):
    """
    :param new_book_for_rent: The new book to be added to the database
    :return: The number of documents in that collection
    """

    all_records = collection_books_for_rent.count_documents({})
    print(all_records)
    all_items_in_library["books"][0]["books_for_rent"].extend(new_book_for_rent)
    create = collection_books_for_rent.insert_many(all_items_in_library["books"][0]["books_for_rent"])
    print(create)
    print(create.acknowledged)
    all_records_01 = collection_books_for_rent.count_documents({})
    print(all_records_01)
    return

create_one(new_book_for_rent)


