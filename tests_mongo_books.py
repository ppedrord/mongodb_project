import pytest
import mongo_utils, mongo_books

input_a = {
    "book": "The Ruins of Gorlan",
    "author": "John Flanagan",
}


test_create = [(input_a, True)]
@pytest.mark.parametrize(["input", "result"], test_create)
def test_create_one(input, result):
    assert mongo_books.create_one(input) == result


