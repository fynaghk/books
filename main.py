import json
def getDataFromDataBase(file_name):
    with open(file_name, "r")  as f:
        return json.load(f)


book_ = getDataFromDataBase("db.json")


def bookPrice(price):
    for price_ in book_['books']:
        if price_['price'] < price:
            print(f"{price_['book']} | {price_['author']}")


you = int(input("Enter book price:"))
bookPrice(you)
