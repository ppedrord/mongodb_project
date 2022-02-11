import pymongo
import mongo_utils


def create_one(collection, input: dict):
    """
        :param new_book_for_rent: The new book to be added to the database
        :return: The number of documents in that collection
    """

    print("to aqui1")
    create = collection.insert_one(input)
    print("to aq")
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


