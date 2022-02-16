import pytest
import mongo_books
from mongo_utils import get_client

client = get_client()

@pytest.fixture
def db_collection():
    collection = client.books
    yield collection
    collection.drop()

@pytest.fixture
def db_collection_create_many():
    collection_customers = client["customers"]
    yield collection_customers
    collection_customers.drop()


@pytest.fixture
def db_create_and_populate_collection_for_tests():
    collection_customers = client["customers"]
    many_customers_list = [
        {
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "payment_status": True
            },
        {
            "_id": "CID0002",
            "customer_name": "João Victor",
            "age": "22",
            "payment_status": False
            },
        {
            "_id": "CID0003",
            "customer_name": "Cristiano",
            "age": "20",
            "payment_status": True
            },
        {
            "_id": "CID0004",
            "customer_name": "Marcelo",
            "age": "29",
            "payment_status": False
            },
        {
            "_id": "CID0005",
            "customer_name": "Ricardo",
            "age": "45",
            "payment_status": True
            }]
    collection_customers.insert_many(many_customers_list)
    yield collection_customers
    collection_customers.drop()


value = {
        "customer_name": "João Victor",
        "age": "22"
    }
def test_create_one(db_collection):
    assert mongo_books.create_one(db_collection, value) == True


many_customers = [
        {
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "payment_status": True
            },
        {
            "_id": "CID0002",
            "customer_name": "João Victor",
            "age": "22",
            "payment_status": False
            },
        {
            "_id": "CID0003",
            "customer_name": "Cristiano",
            "age": "20",
            "payment_status": True
            },
        {
            "_id": "CID0004",
            "customer_name": "Marcelo",
            "age": "29",
            "payment_status": False
            },
        {
            "_id": "CID0005",
            "customer_name": "Ricardo",
            "age": "45",
            "payment_status": True
            }]
def test_create_many(db_collection_create_many):
    assert mongo_books.create_many(db_collection_create_many, many_customers) == True


field_01 = "customer_name"
value_01 = "Pedro Paulo Monteiro Muniz Barbosa"
search_result = {
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "payment_status": True
            }
def test_find_one(db_create_and_populate_collection_for_tests):
    assert mongo_books.find_one(db_create_and_populate_collection_for_tests, field_01, value_01) == search_result


field_many_01 = "age"
modifier_many_01 = "$gt"
value_many_01 = "21"
search_result_find_many = [{
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "payment_status": True
            },
        {
            "_id": "CID0002",
            "customer_name": "João Victor",
            "age": "22",
            "payment_status": False
            },
        {
            "_id": "CID0004",
            "customer_name": "Marcelo",
            "age": "29",
            "payment_status": False
            },
        {
            "_id": "CID0005",
            "customer_name": "Ricardo",
            "age": "45",
            "payment_status": True
            }]
def test_find_many(db_create_and_populate_collection_for_tests):
    assert mongo_books.find_many(db_create_and_populate_collection_for_tests, field_many_01, modifier_many_01,
                                 value_many_01) == search_result_find_many


field_update_one_01 = "customer_name"
value_update_one_01 = "João Victor"
modifier_update_one_01 = "$set"
new_value_update_one_01 = "João Victor Fernandes Maciel da Silva"
def test_update_one(db_create_and_populate_collection_for_tests):
    assert mongo_books.update_one(db_create_and_populate_collection_for_tests, field_update_one_01, value_update_one_01,
                                  modifier_update_one_01, new_value_update_one_01) == 1


field_update_many_01 = "payment_status"
value_update_many_01 = False
modifier_update_many_01 = "$set"
new_value_update_many_01 = True
def test_update_many(db_create_and_populate_collection_for_tests):
    assert mongo_books.update_many(db_create_and_populate_collection_for_tests, field_update_many_01,
                                   value_update_many_01, modifier_update_many_01, new_value_update_many_01) == 2


field_delete_one_01 = "customer_name"
value_delete_one_01 = "Cristiano"
def test_delete_one(db_create_and_populate_collection_for_tests):
    assert mongo_books.delete_one(db_create_and_populate_collection_for_tests, field_delete_one_01,
                                  value_delete_one_01) == 1


field_delete_many_01 = "age"
modifier_delete_many_01 = "$gt"
value_delete_many_01 = "22"
def test_delete_many(db_create_and_populate_collection_for_tests):
    assert mongo_books.delete_many(db_create_and_populate_collection_for_tests, field_delete_many_01,
                                   modifier_delete_many_01, value_delete_many_01) == True


@pytest.fixture
def db_collection_insert_many_multiple_collections():
        client = get_client()
        authors = client.authors

        authors.insert_many([
            {"_id": 1, "name": "Pedro"},
            {"_id": 2, "name": "Lauro"},
            ])

        books = client.books
        books.insert_many([
            {"_id": 1, "id_author": 1, "book": "A Bíblia Comentada"},
            {"_id": 2, "id_author": 2, "book": "Lição Jovem"},
            {"_id": 3, "id_author": 1, "book": "A Bíblia Comentada 2"}
            ])
        yield books
        books.drop()

