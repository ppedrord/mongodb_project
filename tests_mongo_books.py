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
            "customer_name": "Igor",
            "age": "24",
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


@pytest.fixture
def db_collection_insert_many_multiple_collections():
    collection_books_for_rent = client["books_for_rent"]
    books_for_rent = [
        {
            "_id": "U1IT0000001",
            "book_name": "The Road to Serfdom",
            "author": "Friedrich A. Hayek",
            "year": "1944",
            "price": 2.99,
            "category": [
                "Political Science",
                "Economics"
                ],
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000002",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 3.49,
            "category": [
                "Political Science"
                ],
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000003",
            "book_name": "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000004",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000005",
            "book_name": "The Icebound Land",
            "author": "John Flanagan",
            "year": "2005",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            }

        ]
    collection_books_for_rent.insert_many(books_for_rent)
    collection_customers = client["customers"]
    many_customers_list = [
        {
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "id_books_rented": [
                "U1IT0000001",
                "U1IT0000002"
                ],
            "payment_status": False,
            },
        {
            "_id": "CID0002",
            "customer_name": "João Victor",
            "age": "22",
            "id_books_rented": None,
            "payment_status": True
            },
        {
            "_id": "CID0003",
            "customer_name": "Cristiano",
            "age": "20",
            "id_books_rented": [
                "U1IT0000003"
                ],
            "payment_status": False
            },
        {
            "_id": "CID0004",
            "customer_name": "Igor",
            "age": "24",
            "id_books_rented": [
                "U1IT0000004"
                ],
            "payment_status": False
            },
        {
            "_id": "CID0005",
            "customer_name": "Ricardo",
            "age": "45",
            "id_books_rented": [
                "U1IT0000005"
                ],
            "payment_status": False
            }]
    collection_customers.insert_many(many_customers_list)
    yield collection_customers
    collection_customers.drop()
    collection_books_for_rent.drop()


@pytest.fixture
def db_collection_books_check_book_availability_status_in_customer():
    collection_books = client["books"]
    books_for_rent = [
        {
            "_id": "U1IT0000001",
            "book_name": "The Road to Serfdom",
            "author": "Friedrich A. Hayek",
            "year": "1944",
            "price": 2.99,
            "category": [
                "Political Science",
                "Economics"
                ],
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000002",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 3.49,
            "category": [
                "Political Science"
                ],
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000003",
            "book_name": "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000004",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            },
        {
            "_id": "U1IT0000005",
            "book_name": "The Icebound Land",
            "author": "John Flanagan",
            "year": "2005",
            "price": 3.49,
            "category": [
                "Fantasy",
                "Adventure"
                ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent",
            "availability_status": False
            }

        ]
    collection_books.insert_many(books_for_rent)
    yield collection_books
    collection_books.drop()


@pytest.fixture
def db_collection_customers_check_book_availability_status_in_customer():
    collection_customers = client["customers"]
    many_customers_list = [
        {
            "_id": "CID0001",
            "customer_name": "Pedro Paulo Monteiro Muniz Barbosa",
            "age": "22",
            "id_books_rented": [
                "U1IT0000001",
                "U1IT0000002"
                ],
            "payment_status": False,
            },
        {
            "_id": "CID0002",
            "customer_name": "João Victor",
            "age": "22",
            "id_books_rented": None,
            "payment_status": True
            },
        {
            "_id": "CID0003",
            "customer_name": "Cristiano",
            "age": "20",
            "id_books_rented": [
                "U1IT0000003"
                ],
            "payment_status": False
            },
        {
            "_id": "CID0004",
            "customer_name": "Igor",
            "age": "24",
            "id_books_rented": [
                "U1IT0000004"
                ],
            "payment_status": False
            },
        {
            "_id": "CID0005",
            "customer_name": "Ricardo",
            "age": "45",
            "id_books_rented": [
                "U1IT0000005"
                ],
            "payment_status": False
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
        "customer_name": "Igor",
        "age": "24",
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
value_many_01 = "21"
search_result_find_many = [
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
        "_id": "CID0004",
        "customer_name": "Igor",
        "age": "24",
        "payment_status": False
        },
    {
        "_id": "CID0005",
        "customer_name": "Ricardo",
        "age": "45",
        "payment_status": True
        }]


def test_find_many_greater_than(db_create_and_populate_collection_for_tests):
    assert mongo_books.find_many_greater_than(db_create_and_populate_collection_for_tests, field_many_01,
                                              value_many_01) == search_result_find_many


field_update_one_01 = "customer_name"
value_update_one_01 = "João Victor"
new_value_update_one_01 = "João Victor Fernandes Maciel da Silva"


def test_update_one_set(db_create_and_populate_collection_for_tests):
    assert mongo_books.update_one_set(db_create_and_populate_collection_for_tests, field_update_one_01,
                                      value_update_one_01, new_value_update_one_01) == 1


field_update_many_01 = "payment_status"
value_update_many_01 = False
new_value_update_many_01 = True


def test_update_many_set(db_create_and_populate_collection_for_tests):
    assert mongo_books.update_many_set(db_create_and_populate_collection_for_tests, field_update_many_01,
                                       value_update_many_01, new_value_update_many_01) == 2


field_delete_one_01 = "customer_name"
value_delete_one_01 = "Cristiano"


def test_delete_one(db_create_and_populate_collection_for_tests):
    assert mongo_books.delete_one(db_create_and_populate_collection_for_tests, field_delete_one_01,
                                  value_delete_one_01) == 1


field_delete_many_01 = "age"
value_delete_many_01 = "21"


def test_delete_many_greater_than(db_create_and_populate_collection_for_tests):
    assert mongo_books.delete_many_greater_than(db_create_and_populate_collection_for_tests, field_delete_many_01,
                                   value_delete_many_01) == 4


field_update_book_status = "id_books_rented"
value_update_book_status = [
    "U1IT0000001",
    "U1IT0000002"
    ]
new_value_update_book_status = None


def test_update_books_rentend_for_customers(db_collection_insert_many_multiple_collections):
    assert mongo_books.update_one_set(db_collection_insert_many_multiple_collections, field_update_book_status,
                                      value_update_book_status, new_value_update_book_status) == 1


book_name_01 = "The Ruins of Gorlan"


def test_check_book_availability_status_in_customer(db_collection_books_check_book_availability_status_in_customer,
                                                    db_collection_customers_check_book_availability_status_in_customer):
    assert mongo_books.check_book_availability_status_in_customers(
        db_collection_books_check_book_availability_status_in_customer,
        db_collection_customers_check_book_availability_status_in_customer, book_name_01) == False


def test_update_book_availability_status(db_collection_books_check_book_availability_status_in_customer,
                                         db_collection_customers_check_book_availability_status_in_customer):
    assert mongo_books.update_book_availability_status(
        db_collection_books_check_book_availability_status_in_customer,
        db_collection_customers_check_book_availability_status_in_customer, book_name_01) == 2
