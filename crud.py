import json


def getDataFromDataBase(file_name):
    with open(file_name, "r") as f:
        return json.load(f)


book_ = getDataFromDataBase("db.json")


def new_book():
    name = input("Name: ")
    author = input("Author: ")
    year = int(input("Year: "))
    price = int(input("Price: "))
    category_ID = int(input("ID: "))

    books = {
        "name": name,
        "author": author,
        "year": year,
        "price": price,
        "category_ID": category_ID
    }

    book_["books"].append(books)
    with open("db.json", "a") as f:
        json.dump(book_, f)


user = new_book()
