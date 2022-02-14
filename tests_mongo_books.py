import pytest
import mongo_books
from mongo_utils import get_client


@pytest.fixture
def create_collection():
    print("Creating collection 'customers...")
    collection_customers = get_client().customers
    print("'customers' collection was created!\n")
    return collection_customers


@pytest.fixture
def insert_data_and_drop_collection(create_collection):
    input_data = {
        "customer_name": "Douglas",
        "age": "22",
    }
    data_inserted = create_collection().insert_one(input_data)
    yield data_inserted
    print("Dropping 'customers' collection...")
    collection_customers.drop()
    print("'customers' collection was deleted!")


input_many_documents = [
        {
            "customer_name": "Pedro Paulo",
            "age": "22"
        },
        {
            "customer_name": "João Victor",
            "age": "22"
        }
  ]
result = [(create_collection(), insert_data_and_drop_collection(), True)]


@pytest.mark.parametrize(["collection", "input_data", "expected"], result)
def test_create_one(collection, input_data):
    assert mongo_books.create_one(collection, input_data) == True
