import pymongo
from mongo_utils import get_client


def create_one(collection: pymongo.collection.Collection, input_data: dict) -> bool:
    """
    :param collection: A collection to be updated
    :param input_data: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection.insert_one(input_data)

    return create.acknowledged


def create_many(collection: pymongo.collection.Collection, input_many_documents: list) -> bool:
    """
    :param collection: A collection to be updated
    :param input_many_documents: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection.insert_many(input_many_documents)
    return create.acknowledged


def find_one(collection: pymongo.collection.Collection, field: str, value: str) -> dict:
    """
    :param collection: The collection that will be read
    :param field: The field being searched
    :param value: The value being searched
    :return: A document with the specified parameter
    """
    find = collection.find_one({field: value})
    return find


def find_many_greater_than(collection: pymongo.collection.Collection, field: str,
                           value: str or dict or int or bool) -> list:
    """
    :param value: The value being searched
    :param field: The field being searched
    :param collection: The collection that will be read
    :return: A list of occurrences with the specified parameters
    """
    list_of_occurrence = []
    find_many_documents = collection.find({field: {"$gt": value}})
    for occurrences in find_many_documents:
        list_of_occurrence.append(occurrences)
    return list_of_occurrence


def update_one_set(collection: pymongo.collection.Collection, field: str, value: str or dict,
                   new_value: str or dict or int or bool) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param new_value: The new value after the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """
    update_one_document = collection.update_one({field: value}, {"$set": {field: new_value}})
    return update_one_document.modified_count


def update_many_set(collection: pymongo.collection.Collection, field: str, value: str or dict,
                    new_value: str or dict or int or bool) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param new_value: The new value after the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """
    update_many_documents = collection.update_many({field: value}, {"$set": {field: new_value}})
    return update_many_documents.modified_count


def delete_one(collection: pymongo.collection.Collection, field: str, value: str or dict or int or bool) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param collection: The collection that will be read
    :return: The number of deleted documents
    """
    delete_document = collection.delete_one({field: value})
    return delete_document.deleted_count


def delete_many(collection: pymongo.collection.Collection, field: str, value: str or dict or int or bool,
                modifier: str, ) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param modifier: The modifier to do the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """

    delete_many_documents = collection.delete_many({field: {modifier: value}})
    return delete_many_documents.acknowledged


def check_book_availability_status_in_customers(collection_books: pymongo.collection.Collection,
                                                collection_customers: pymongo.collection.Collection,
                                                book_name: str) -> bool:
    """
    :param collection_books: The collection of books in the Library
    :param collection_customers: The customers registered in the Library
    :param book_name: The name of the book to be searched
    :return: True if the book is available for rent and False if it's not
    """
    find_book = collection_books.find_one({"book_name": book_name}, {"_id": 1})
    book_id = find_book.get("_id")
    documents_in_collection_customers = []
    result = bool

    for document in collection_customers.find({}):
        documents_in_collection_customers.append(document)

    for i, v in enumerate(documents_in_collection_customers):
        try:
            if book_id in v["id_books_rented"]:
                result = collection_books.find_one({"book_name": book_name}, {"availability_status": 1})
                result = result.get("availability_status")
        except TypeError:
            print("TypeError: argument of type 'NoneType' is not iterable")

    return result
