import pymongo
from mongo_utils import get_client

collection = get_client()["customers"]
input_data = {
        "customer_name": "Douglas",
        "age": "22",
    }


def create_one(collection: pymongo.collection.Collection, input_data: dict = None) -> bool:
    """
    :param collection: A collection to be updated
    :param input_data: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection.insert_one(input_data)
    return create.acknowledged


create_one(collection, input_data)


input_many_documents = [
        {
            "customer_name": "Pedro Paulo Monteiro Muniz",
            "age": "22"
        },
        {
            "customer_name": "João Victor",
            "age": "22"
        },
        {
            "customer_name": "Cristiano",
            "age": "20"
        },
        {
            "customer_name": "Marcelo",
            "age": "29"
        },
        {
            "customer_name": "Ricardo",
            "age": "45"
        }
  ]


def create_many(collection: pymongo.collection.Collection, input_many_documents: list = None) -> bool:
    """
    :param collection: A collection to be updated
    :param input_many_documents: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection.insert_many(input_many_documents)
    return create.acknowledged


create_many(collection, input_many_documents)
print("Number of elements after create all documents:\n", collection.count_documents({}), "\n")

query_find_one = {"customer_name": "Pedro Paulo Monteiro Muniz"}


def find_one(collection: pymongo.collection.Collection, query_find_one: dict = None) -> dict:
    """
    :param collection: The collection that will be read
    :param query_find_one: The parameter for the search with field and value
    :return: A document with the specified parameter
    """
    find = collection.find_one(query_find_one)
    return find


print("find_one:\n", find_one(collection, query_find_one), "\n")


query_find_many = {"age": {"$gt": "21"}}


def find_many(collection: pymongo.collection.Collection, query_find_many: dict = None) -> list:
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


print("find_many:\n", find_many(collection, query_find_many), "\n")


query_delete_one = {"customer_name": "Douglas"}


def delete_one(collection: pymongo.collection.Collection, query_delete_one: dict = None) -> dict:
    """
    :param collection: The collection that will be read
    :param query_find_one: The parameter for the search with field and value
    :return: A document with the specified parameter
    """
    find = collection.find_one(query_delete_one)
    print(find)
    delete_document = collection.delete_one(query_delete_one)
    return delete_document


print("delete_one:\n", delete_one(collection, query_delete_one), "\n")
print("Number of documents after the method 'delete_one':\n", collection.count_documents({}), "\n")

query_delete_many = query_find_many = {"age": {"$gt": "22"}}


def delete_many(collection: pymongo.collection.Collection, query_delete_many: dict = None) -> list:
    """
    :param collection: The collection that will be read
    :param query_find_many: The parameter for the search with field and value
    :return: A list of occurrences with the specified parameters
    """
    list_of_occurrence_to_delete = []
    find_many_documents = collection.find(query_delete_many)
    for occurrences in find_many_documents:
        list_of_occurrence_to_delete.append(occurrences)
    delete_many_documents = collection.delete_many(query_delete_many)
    print(delete_many_documents)
    return list_of_occurrence_to_delete


print("delete_many:\n", delete_many(collection, query_delete_many))
print("Number of documents after the method 'delete_many':\n", collection.count_documents({}), "\n")