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

def find_one(collection: pymongo.collection.Collection, field :str, value :str) -> dict:
    """
    :param collection: The collection that will be read
    :param field: The field being searched
    :param value: The value being searched
    :return: A document with the specified parameter
    """
    find = collection.find_one({field: value})
    return find

def find_many(collection: pymongo.collection.Collection, query_find_many: dict) -> list:
    """
    :param collection: The collection that will be read
    :param query_find_many: The parameter for the search with field and value
    :return: A list of occurrences with the specified parameters
    """
    list_of_occurrence = []
    find_many_documents = collection.find(query_find_many)
    for occurrences in find_many_documents:
        list_of_occurrence.append(occurrences)
    return list_of_occurrence

def update_one(collection: pymongo.collection.Collection, query_update_one: dict, data_update_one: dict) -> int:
    """
    :param collection: The collection that will be updated
    :param query_update_one: The parameters to found the document that will be updated
    :param data_update_one: The new data to update the document
    :return: The number of modified documents
    """
    update_one_document = collection.update_one(query_update_one, data_update_one)
    return update_one_document.modified_count

def update_many(collection: pymongo.collection.Collection, query_update_many: dict, data_update_many: dict) -> int:
    """
    :param collection: The collection that will be updated
    :param query_update_many: The parameters to found the documents that will be updated
    :param data_update_many: The new data to update the documents
    :return: The number of modified documents
    """
    update_many_documents = collection.update_many(query_update_many, data_update_many)
    return update_many_documents.modified_count

def delete_one(collection: pymongo.collection.Collection, query_delete_one: dict) -> int:
    """
    :param collection: The collection that will be read
    :param query_delete_one: The parameter for the search with field and value
    :return: The number of deleted documents
    """
    find = collection.find_one(query_delete_one)
    delete_document = collection.delete_one(query_delete_one)
    return delete_document.deleted_count

def delete_many(collection: pymongo.collection.Collection, query_delete_many: dict) -> int:
    """
    :param collection: The collection that will be read
    :param query_delete_many: The parameter for the search with field and value
    :return: The number of deleted documents
    """
    list_of_occurrence_to_delete = []
    find_many_documents = collection.find(query_delete_many)
    for occurrences in find_many_documents:
        list_of_occurrence_to_delete.append(occurrences)
    print(list_of_occurrence_to_delete)
    delete_many_documents = collection.delete_many(query_delete_many)
    return delete_many_documents.deleted_count

def drop_collection(collection: pymongo.collection.Collection) -> None:
    dropping_collection = collection.drop()
    return dropping_collection

