from classes import book
from storage import *
from menus import admin_menu, main_menu, member_menu
import os


password = 1234
accounts = load_accounts()
book.load_books()
while True:
    main_menu()
    request = int(input(""))
    if request == 1:
        pin = input("Enter your pin: ").strip()
        pin = int(pin)
        if pin == password:
            admin_menu()
            request = int(input(""))
            if request == 1:
                name_of_book = input("Enter name of book: ").lower().strip()
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

            elif request == 6:
                user_input = input("Enter the username: ").strip().lower()

                for uname in list(accounts.keys()):
                    if uname == user_input:   
                        del accounts[uname]    
                        print(f"{uname} deleted successfully")
                        save_accounts(accounts)

            elif request == 7:
                print(accounts)

            else:
                print("Enter a valid input")
                continue
        
        else:
            print("Your pin is wrong, enter the valid pin")
            continue

    elif request == 2:
        account_name = input("Enter account name: ").strip()
        if account_name in accounts:
            pin = input("Pin: ")
            if pin == accounts[account_name]:
                print("Congratulations, you have successfully logged in!")
                member_menu()   
                request = input("").strip()
                request = int(request)
                if request == 1:
                    print(list(book.books.items()))

                elif request == 2:
                    book_name = input("Enter the name of book: ").strip().lower()
                    if book_name in book.books:
                        print(f"{book_name} is availble")
                        request = input("Press y to read book: ").lower().strip()
                        if request == "y":
                            pdf_path = f"{book_name}.pdf"
                            os.startfile(pdf_path)

                        else:
                            continue
                    else:
                        print(f"Sorry we do not have{book_name} available")
                elif request == 3:
                    continue
                
                else:
                    print("Input invalid")
                    break      

        else:
            print("Your account does not exist")
    
    elif request == 3:
        account_name = input("Enter account name: ")
        pin = input("Enter pin: ")
        pin1 = input("Confirm pin: ")
        accounts[account_name] = pin
        if pin == pin1:
            print(f"Congratulations, {account_name} you have created a new account!!")
            save_accounts(accounts)

        else:
            print("Pins do not match!!")

    elif request == 4:
        print("Thank you for using the Royal Library System!")
        break

    else: 
        print("Enter a valid input")
        break