import pymongo
import mongo_utils

db = mongo_utils.get_client()

def create_one(input: dict):
    """
        :param new_book_for_rent: The new book to be added to the database
        :return: The number of documents in that collection
    """

    books = db.books

    create = books.insert_one(input)

    return create.acknowledged

def create_many():
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
    return ''


input_a = {
    "book": "The Ruins of Gorlan",
    "author": "John Flanagan",
}

create_one(input_a)


