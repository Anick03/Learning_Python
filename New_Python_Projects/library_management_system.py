import time

#Initializing an empty dictionary to store book inventory
library = {}

# Defining functions for library management system
def add_book():
    book = input("Enter the book name: ")
    quantity = int(input("Enter quantity: "))
    if book in library:
        library[book] += quantity
    else:
        library[book] = quantity
    print(f"{quantity} copies of \"{book}\" added successfully.\n")

def view_books():
    if not library:
        print("Book inventory is empty.\n")
        return
    print("\nAvailable Books:")
    for book, quantity in library.items():
        print(f"{book} : {quantity} copies")
    print()

def borrow_book():
    book = input("Enter book name to borrow: ")

    if book in library and library[book] > 0:
        library[book] -= 1
        print(f"You borrowed \"{book}\".\n")
    else:
        print("Book not available.\n")

def return_book():
    book = input("Enter the name of the book to return: ")
    if book in library:
        library[book] += 1
    else:
        library[book] = 1
    print(f"\"{book}\" returned successfully.\n")

# Using while loop for the library management system
while True:
    print("===== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    # Asking user for their choice
    choice = input("Enter your choice: ")

    # Performing actions based on user choice using conditional statement
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.\n")
        
    #Adding two seconds delay for better user experience
    time.sleep(2)  