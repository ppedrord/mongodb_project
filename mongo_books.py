import pymongo
from mongo_utils import get_client

collection_created = get_client()["customers"]
input_data = {
        "customer_name": "Douglas",
        "age": "22",
        "payment_status": False
    }


def create_one(collection_created: pymongo.collection.Collection, input_data: dict = None) -> bool:
    """
    :param collection_created: A collection to be updated
    :param input_data: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection_created.insert_one(input_data)
    return create.acknowledged


create_one(collection_created, input_data)


input_many_documents = [
        {
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "payment_status": True
        },
        {
            "customer_name": "João Victor",
            "age": "22",
            "payment_status": False
        },
        {
            "customer_name": "Cristiano",
            "age": "20",
            "payment_status": True
        },
        {
            "customer_name": "Marcelo",
            "age": "29",
            "payment_status": False
        },
        {
            "customer_name": "Ricardo",
            "age": "45",
            "payment_status": True
        }
  ]


def create_many(collection_created: pymongo.collection.Collection, input_many_documents: list = None) -> bool:
    """
    :param collection_created: A collection to be updated
    :param input_many_documents: The data to be inserted in the database
    :return: True if the writing operation was made
    """
    create = collection_created.insert_many(input_many_documents)
    return create.acknowledged


create_many(collection_created, input_many_documents)
print("Number of elements after create all documents:\n", collection_created.count_documents({}), "\n")

query_find_one = {"customer_name": "Pedro Paulo Monteiro Muniz"}


def find_one(collection_created: pymongo.collection.Collection, query_find_one: dict = None) -> dict:
    """
    :param collection_created: The collection that will be read
    :param query_find_one: The parameter for the search with field and value
    :return: A document with the specified parameter
    """
    find = collection_created.find_one(query_find_one)
    return find


print("find_one:\n", find_one(collection_created, query_find_one), "\n")


query_find_many = {"age": {"$gt": "21"}}


def find_many(collection_created: pymongo.collection.Collection, query_find_many: dict = None) -> list:
    """
    :param collection_created: The collection that will be read
    :param query_find_many: The parameter for the search with field and value
    :return: A list of occurrences with the specified parameters
    """
    list_of_occurrence = []
    find_many_documents = collection_created.find(query_find_many)
    for occurrences in find_many_documents:
        list_of_occurrence.append(occurrences)
    return list_of_occurrence


print("find_many:\n", find_many(collection_created, query_find_many), "\n")


breakpoint()


query_update_one = {"customer_name": "João Victor"}
data_update_one = {"$set": {"customer_name": "João Victor Fernandes Maciel da Silva"}}


def update_one(collection_created: pymongo.collection.Collection, query_update_one: dict = None, data_update_one: dict = None) -> int:
    """
    :param collection_created: The collection that will be updated
    :param query_update_one: The parameters to found the document that will be updated
    :param data_update_one: The new data to update the document
    :return: The number of modified documents
    """
    update_one_document = collection_created.update_one(query_update_one, data_update_one)
    return update_one_document.modified_count


print("update_one:\n", update_one(collection_created, query_update_one, data_update_one), "updated document\n")

breakpoint()

query_update_many = {"payment_status": False}
data_update_many = {"$set": {"payment_status": True}}


def update_many(collection_created: pymongo.collection.Collection, query_update_many: dict = None, data_update_many: dict = None) -> int:
    """
    :param collection_created: The collection that will be updated
    :param query_update_many: The parameters to found the documents that will be updated
    :param data_update_many: The new data to update the documents
    :return: The number of modified documents
    """
    update_many_documents = collection_created.update_many(query_update_many, data_update_many)
    return update_many_documents.modified_count


print("update_many:\n", update_many(collection_created, query_update_many, data_update_many), "updated documents\n")

print("Number of documents before the method 'delete_one':\n", collection_created.count_documents({}), "\n")
breakpoint()
query_delete_one = {"customer_name": "Douglas"}


def delete_one(collection_created: pymongo.collection.Collection, query_delete_one: dict = None) -> int:
    """
    :param collection_created: The collection that will be read
    :param query_delete_one: The parameter for the search with field and value
    :return: The number of deleted documents
    """
    find = collection_created.find_one(query_delete_one)
    print(find)
    delete_document = collection_created.delete_one(query_delete_one)
    return delete_document.deleted_count


print("delete_one:\n", delete_one(collection_created, query_delete_one), "deleted document\n")
print("Number of documents after the method 'delete_one':\n", collection_created.count_documents({}), "\n")

breakpoint()

query_delete_many = {"age": {"$gt": "22"}}


def delete_many(collection_created: pymongo.collection.Collection, query_delete_many: dict = None) -> int:
    """
    :param collection_created: The collection that will be read
    :param query_delete_many: The parameter for the search with field and value
    :return: The number of deleted documents
    """
    list_of_occurrence_to_delete = []
    find_many_documents = collection_created.find(query_delete_many)
    for occurrences in find_many_documents:
        list_of_occurrence_to_delete.append(occurrences)
    print(list_of_occurrence_to_delete)
    delete_many_documents = collection_created.delete_many(query_delete_many)
    return delete_many_documents.deleted_count


print("delete_many:\n", delete_many(collection_created, query_delete_many), "deleted documents\n")
print("Number of documents after the method 'delete_many':\n", collection_created.count_documents({}), "\n")

breakpoint()


def drop_collection(collection_created: pymongo.collection.Collection) -> None:
    dropping_collection = collection_created.drop()
    return dropping_collection


drop_collection(collection_created)
