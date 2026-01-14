import json
import os

class book:
    FILE_NAME = "books.json"
    books = {}

    @classmethod
    def load_books(cls):
        if os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, "r") as file:
                cls.books = json.load(file)
        else:
            cls.books = {}

    @classmethod
    def save_books(cls):
        with open(cls.FILE_NAME, "w") as file:
            json.dump(cls.books, file, indent=4)

accounts = {
    "account_name":"pin"
}



FILE_NAME = "accounts.json"

def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


