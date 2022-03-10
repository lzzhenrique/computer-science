from pymongo import MongoClient


def findBooksByCategorie(categorie):
    client = MongoClient()

    dbname = client.library

    collection_name = dbname["sales"]

    books = collection_name.find(
        {
            "categories": categorie
        }
    )
    for book in books:
        print(book)

    client.close()


findBooksByCategorie('Java')