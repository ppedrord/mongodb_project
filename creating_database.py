from mongo_utils import get_client

dbname = get_client()

all_items_in_library = {
    "items": [
        {
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
                }
            ],
            "items_for_sale": [
                {
                    "_id": "IFS0001",
                    "item_name": "Post-it Notes",
                    "price": 5.99,
                    "color": "Jaipur Collection",
                    "shape": "Square",
                    "material_type": "Paper",
                    "size": "14 Pads",
                    "sheet_size": "3-x-3-inch",
                    "item_category": "Item for Sale"
                }
            ]
        }
    ]
}

collection_books_for_rent = dbname["books_for_rent"]
collection_books_for_rent.insert_many(all_items_in_library["items"][0]["books_for_rent"])

collection_books_for_sale = dbname["books_for_sale"]
collection_books_for_sale.insert_many(all_items_in_library["items"][0]["books_for_sale"])

collection_items_for_sale = dbname["items_for_sale"]
collection_items_for_sale.insert_many(all_items_in_library["items"][0]["items_for_sale"])