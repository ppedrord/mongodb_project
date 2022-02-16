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


def find_many(collection: pymongo.collection.Collection, field: str, modifier: str,
              value: str or dict or int or bool) -> list:
    """
    :param modifier: The modifier to do the operation
    :param value: The value being searched
    :param field: The field being searched
    :param collection: The collection that will be read
    :return: A list of occurrences with the specified parameters
    """
    list_of_occurrence = []
    find_many_documents = collection.find({field: {modifier: value}})
    for occurrences in find_many_documents:
        list_of_occurrence.append(occurrences)
    return list_of_occurrence


def update_one(collection: pymongo.collection.Collection, field: str, value: str or dict, modifier: str,
               new_value: str or dict or int or bool) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param modifier: The modifier to do the operation
    :param new_value: The new value after the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """
    update_one_document = collection.update_one({field: value}, {modifier: {field: new_value}})
    return update_one_document.modified_count


def update_many(collection: pymongo.collection.Collection, field: str, value: str or dict, modifier: str,
                new_value: str or dict or int or bool) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param modifier: The modifier to do the operation
    :param new_value: The new value after the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """
    update_many_documents = collection.update_many({field: value}, {modifier: {field: new_value}})
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
                modifier: str,) -> int:
    """
    :param field: The field being searched
    :param value: The value being searched
    :param modifier: The modifier to do the operation
    :param collection: The collection that will be updated
    :return: The number of modified documents
    """

    delete_many_documents = collection.delete_many({field: {modifier: value}})
    return delete_many_documents.acknowledged
