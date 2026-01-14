from classes import book
from storage import *

while True:
    book.load_books()
    print("Welcome To Your Library Management System")
    print("-------------------------------------------")
    print("1. Administrator")
    print("2. Member")
    print("3. Sign Up")
    print("4. Log Out")

    request = int(input(""))
    if request == 1:
        print("Welcome Admin")
        print("---------------")
        print("1. Add Books")
        print("2. Remove books")
        print("3. Update number of books")
        print("4. View Books")
        print("5. Back")
        request = int(input(""))
        if request == 1:
            name_of_book = input("Enter name of book: ").lower()
            quantity = input(f"Nuber of ({name_of_book}) available: ")
            book.books[name_of_book] = quantity
            print(f"Congratulations {name_of_book} has been successfully added")
            book.save_books()
            continue

        elif request == 2:
            name_of_book = input("Enter the name of the book: ").lower()
            book.books.pop(name_of_book)
            print(f"Congratulations, you have successfully deleted {name_of_book} ")
            book.save_books()
            continue

        elif request == 3:
            name_of_book = input("Enter the name of the book: ").strip()
            new_number_of_books = input("Enter the new number of books: ").strip()
            new_number_of_books = int((new_number_of_books))
            book.books[name_of_book] = new_number_of_books
            print(f"Congratulations, the number has been successfully updated!")
            book.save_books()
            continue

        elif request == 4:
            print(book.books)

        elif request == 5:
            pass

        else:
            print("Enter a valid input")
            continue

    elif request == 2:
        print("Feature still under development")
        continue

    elif request == 3:
        print("Feature still under development")
        continue

    elif request == 4:
        break

    else: 
        print("Enter a valid input")
        break