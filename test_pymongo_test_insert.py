import pymongodb_test_insert
import pytest
from pymongodb_test_insert import get_database

@pytest.fixture(autouse=True)
def test_get_database():
    return get_database()


@pytest.fixture
def create_and_delete_collections():
    dbname_01 = get_database()
    collection_books_for_rent = dbname_01["books_for_rent"]
    collection_books_for_sale = dbname_01["books_for_sale"]
    collection_items_for_sale = dbname_01["items_for_sale"]
    yield collection_books_for_rent, collection_books_for_sale, collection_items_for_sale
    print("Dropping the Collection 'books_for_rent'...")
    collection_books_for_rent.drop()
    print("Done!\n")
    print("Dropping the Collection 'books_for_sale'...")
    collection_books_for_sale.drop()
    print("Done!\n")
    print("Dropping the Collection 'items_for_sale'...")
    collection_items_for_sale.drop()
    print("Done!")


new_books_for_rent_01 = [
        {
            "_id": "U1IT0000003",
            "book_name": "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        },
        {
            "_id": "U1IT0000004",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        }
    ]
new_books_for_sale_01 = [
        {
            "_id": "BFS0002",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for sale"
        },
        {
            "_id": "BFS0003",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 34.99,
            "category": [
                "Political Science"
            ],
            "item_category": "Book for sale"
        }
    ]
new_items_for_sale_01 = [
        {
            "_id": "IFS0002",
            "item_name": "TICONDEROGA Pencils, Wood-Cased, Pre-Sharpened, Graphite",
            "price": 5.99,
            "color": "Yellow",
            "manufacturer": "Dixon Ticonderoga",
            "hardness": "HB",
            "size": "30 Count",
            "point_type": "Fine",
            "ink_color": "Black",
            "item_category": "Item for sale"
        }
    ]

new_database_expected = {
        "books":   [{
                        "books_for_rent": [
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
            "item_category": "Book for rent"
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
            "item_category": "Book for rent"
        },
                                            {
            "_id": "U1IT0000003",
            "book_name": "The Ruins of Gorlan",
            "author": "John Flanagan",
            "year": "2004",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        },
                                            {
            "_id": "U1IT0000004",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for rent"
        }
                                          ],
                        "books_for_sale": [
                                            {
        "_id": "BFS0001",
        "book_name": "The Ruins of Gorlan",
        "author": "John Flanagan",
        "year": "2004",
        "price": 30.00,
        "category": [
            "Fantasy",
            "Adventure"
        ],
        "series": "Ranger's Apprentice",
        "item_category": "Book for sale"
    }, {
            "_id": "BFS0002",
            "book_name": "The Burning Bridge",
            "author": "John Flanagan",
            "year": "2005",
            "price": 30.00,
            "category": [
                "Fantasy",
                "Adventure"
            ],
            "series": "Ranger's Apprentice",
            "item_category": "Book for sale"
        },
                                            {
            "_id": "BFS0003",
            "book_name": "The Ethics of Liberty",
            "author": "Murray N. Rothbard",
            "year": "1982",
            "price": 34.99,
            "category": [
                "Political Science"
            ],
            "item_category": "Book for sale"
        }
                                          ]
                    }
                   ],
        "items": [
                    {
                        "items_for_sale": [{
            "_id": "IFS0001",
            "item_name": "Post-it Notes",
            "price": 5.99,
            "color": "Jaipur Collection",
            "shape": "Square",
            "material_type": "Paper",
            "size": "14 Pads",
            "sheet_size": "3-x-3-inch",
            "item_category": "Item for Sale"
        },
                            {
                "_id": "IFS0002",
                "item_name": "TICONDEROGA Pencils, Wood-Cased, Pre-Sharpened, Graphite",
                "price": 5.99,
                "color": "Yellow",
                "manufacturer": "Dixon Ticonderoga",
                "hardness": "HB",
                "size": "30 Count",
                "point_type": "Fine",
                "ink_color": "Black",
                "item_category": "Item for sale"
            }]
        }
                 ]
    }

test_01 = [(new_books_for_rent_01, new_books_for_sale_01, new_items_for_sale_01, new_database_expected)]


@pytest.mark.parametrize(["new_books_for_rent", "new_books_for_sale", "new_items_for_sale", "expected"], test_01)
def test_method_to_add_items_to_the_database(create_and_delete_collections, new_books_for_rent, new_books_for_sale, new_items_for_sale, expected):
    assert pymongodb_test_insert.method_to_add_items_to_the_database(new_books_for_rent, new_books_for_sale, new_items_for_sale) == expected