import pytest
import mongo_books_new
from mongo_utils import get_client

@pytest.fixture
def db_collection():
    client     = get_client()
    collection = client.books
    yield collection
    collection.drop()

@pytest.fixture
def db_collection_insert_many():
    client     = get_client()
    collection = client.books
    collection.insert_many([
        {"_id": 1, "name": "Pedro", "book": "A Bíblia Comentada"},
        {"_id": 2, "name": "Lauro", "book": "Lição Jovem"},
        {"_id": 3, "name": "Pedro", "book": "A Bíblia Comentada 2"}
    ])
    yield collection
    collection.drop()

value = {
        "customer_name": "João Victor",
        "age": "22"
    }
def test_create_one(db_collection):
    assert mongo_books_new.create_one(db_collection, value) == True

many_values = [
        {
            "customer_name": "Pedro Paulo",
            "age": "22"
        },
        {
            "customer_name": "João Victor",
            "age": "22"
        }
  ]
def test_create_many(db_collection):
    assert mongo_books_new.create_many(db_collection, many_values) == True


output_find_one_Pedro = {"_id": 1, "name": "Pedro", "book": "A Bíblia Comentada"}
output_find_one_Lauro = {"_id": 2, "name": "Lauro", "book": "Lição Jovem"}
def test_find_one(db_collection_insert_many):
    assert mongo_books_new.find_one(db_collection_insert_many, "name", "Pedro") == output_find_one_Pedro
    assert mongo_books_new.find_one(db_collection_insert_many, "name", "Lauro") == output_find_one_Lauro