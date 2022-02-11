import pytest
import mongo_utils, mongo_books

@pytest.fixture
def get_client_test():
    db = mongo_utils.get_client()
    return db


@pytest.fixture
def collection_func(get_client_test):
    collection = get_client_test().books
    yield collection
    print("Dropping the Collection 'books_for_rent'...")
    collection.drop()
    print("Done!\n")


input_a = {
    "book": "The Ruins of Gorlan",
    "author": "John Flanagan",
}


def test_create_one():
    assert mongo_books.create_one(collection_func, input_a) == True


