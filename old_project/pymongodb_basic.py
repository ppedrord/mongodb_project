from pymongo import MongoClient

def get_client():
    # Use the atlas url to connect pyhton to MongoDB using pymong
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9"

    # Create a connection using MongoClient
    client = MongoClient(connection_string)
    return client['library_database']

dbname = get_client()

collection_books_for_rent = dbname["books_for_rent"]
collection_books_for_sale = dbname["books_for_sale"]
collection_items_for_sale = dbname["items_for_sale"]

all_items_in_library = {
  "books": [
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
      ]
    }
  ],
  "items": [
    {
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