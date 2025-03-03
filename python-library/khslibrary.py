import time

## USER DATABASE
users = {
    'sgilmore': 'Pass1',
    'bwiseman': 'Pass2',
    'uhalaj': 'Pass3',
    'gwang': 'Pass4',
    'mkassar': 'Pass5',
    'adib': 'Pass6',
    'bwiseman': 'Pass7',
    'kjohnson': 'Pass8',
    'fjose': 'Pass9',
    'mmansour': 'Pass10',
}

fullnames = {
    'sgilmore': 'Sam Gilmore', 
    'bwiseman': 'Bella Wiseman',
    'uhalaj': 'Umar Halaj',
    'gwang': 'Qing Wang',
    'mkassar': 'Maryam Kassar',
    'adib': 'Ali Dib',
    'bwiseman': 'Benji Wiseman',
    'kjohnson': 'Khadija Johnson',
    'fjose': 'Fiona Jose',
    'mmansour': 'Mathew Mansour',
}

print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("Welcome to Kingsgrove High School's library services.")

## login
def login():
    attempts=3
    while attempts > 0:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        if username in users and users[username] == password:
            print("Login successful! Welcome, {}!".format(fullnames[username]))
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print("..........................")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("..........................")
            print("....||..............||....")
            print("....||..............||....")
            print("....||..............||....")
            print("....||..............||....")
            print("....==================....")
            print("..........................")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            return username
        attempts -= 1
        print("Incorrect username or password. Please try again. You have {} attempts left.".format(attempts))
    if attempts == 0:
        print("Too many failed login attempts. Please rerun program and try again.")
        return

# Keep username to obtain full name
username = login()
fullname = (fullnames[username])

## FULL BOOK DATABASE
books = {
    "1101": ("In Search of Lost Time", "t"),
    "1102": ("Ulysses", "t"),
    "1103": ("Don Quixote", "t"),
    "1104": ("The Great Gatsby", "f"),
    "1105": ("Moby Dick", "f"),
    "1106": ("One Hundred Years of Solitude", "t"),
    "1107": ("War and Peace", "f"),
    "1108": ("Hamlet", "f"),
    "1109": ("Lolita", "t"),
    "1110": ("The Odyssey", "t"),
    "1111": ("The Brothers Karamazov", "f"),
    "1112": ("The Adventures of Huckleberry Finn", "f"),
    "1113": ("Madame Bovary", "t"),
    "1114": ("The Catcher in the Rye", "t"),
    "1115": ("The Divine Comedy", "f")
}

available_books = {code: info for code, info in books.items() if info[1] == 't'}
unavailable_books = {code: info for code, info in books.items() if info[1] == 'f'}

while True:
    print("\nWelcome to Kingsgrove High School's Library, {}!".format(fullnames[username]))
    print("Please choose a service from the menu below:")
    print("1. List all books in the library")
    print("2. List all available books in the library")
    print("3. Borrow a book from the library")
    print("4. Return a book to the library")
    print("5. Exit the library")
    for _ in range(5):
        print(".")
    operation = input("Enter the number corresponding to your choice: ")

    if operation == "1":
        print("Fetching the list of all books. Please wait...")
        print(".")
        print(".")
        print(".")
        print("**LIST OF ALL BOOKS**")
        for idx, (book_code, book_info) in enumerate(books.items(), start=1):
            title = book_info[0]
            print(f"{idx}. {title} (Book Code: {book_code})")
        print(f"\nThere are a total of {len(books)} books")
        time.sleep(5)

    elif operation == "2":
        print("Fetching the list of available books. Please wait...")
        print(".")
        print(".")
        print(".")
        print("**LIST OF AVAILABLE BOOKS**")
        if not available_books:
            print("No books are currently available for borrowing.")
        else:
            for idx, (book_code, book_info) in enumerate(available_books.items(), start=1):
                print(f"{idx}. {book_info[0]} (Book Code: {book_code})")
            print(f"\nThere are a total of {len(available_books)} books available.")
        time.sleep(5)

    elif operation == "3":
        print("Opening available books to borrow...\n")
        print("**LIST OF AVAILABLE BOOKS TO BORROW**")
        if not available_books:
            print("No books are currently available for borrowing.")
        else:
            for idx, (book_code, book_info) in enumerate(available_books.items(), start=1):
                print(f"{idx}. {book_info[0]} (Book Code: {book_code})")
            print(f"\nThere are a total of {len(available_books)} books available.")
            bookofchoice = input("\nPlease enter the book code of the book you wish to borrow: ")
            if bookofchoice in available_books:
                print("Book found!")
                print("Confirm borrow {} - {}? (y/n)".format(bookofchoice, available_books[bookofchoice][0]))
                confirm = input()
                if confirm.lower() == "y":
                    print("Successful request. Your request will be processed within 1-3 school days and you will be notified via your @education.nsw.gov.au email regarding your request.")
                else:
                    print("Borrow cancelled.")
            else:
                if bookofchoice in unavailable_books:
                    print("Sorry, the book is currently not available.")
                else:
                    print("The book code does not exist. Please check the code and try again.")
        time.sleep(5)

    elif operation == "4":
        print("Opening available books to return...\n")
        print("**LIST OF AVAILABLE BOOKS TO RETURN**")
        if not available_books:
            print("No books are currently available for returning.")
        else:
            for idx, (book_code, book_info) in enumerate(unavailable_books.items(), start=1):
                print(f"{idx}. {book_info[0]} (Book Code: {book_code})")
            print(f"\nThere are a total of {len(unavailable_books)} books available to return.")
            bookofchoice = input("\nPlease enter the book code of the book you wish to return: ")
            if bookofchoice in unavailable_books:
                print("Book found!")
                print("Confirm return {} - {}? (y/n)".format(bookofchoice, unavailable_books[bookofchoice][0]))
                confirm = input()
                if confirm.lower() == "y":
                    print("Successful request. Your request will be processed within 1-3 school days and you will be notified via your @education.nsw.gov.au email regarding your request.")
                else:
                    print("Borrow cancelled.")
            else:
                if bookofchoice in unavailable_books:
                    print("Sorry, the book is currently not available.")
                else:
                    print("The book code does not exist. Please check the code and try again.")
        time.sleep(5)

    elif operation == "5":
        confirm_exit = input("Are you sure you want to exit? (y/n): ")
        if confirm_exit.lower() == "y":
            print("Thank you for using Kingsgrove High School's library services, {}!".format(fullnames[username]))
            print("Developed by Hanly Wijaya, 2025")
            print("All rights reserved, 2025 HANLY WIJAYA ©")
            print("\n" * 2)
            print("..........................")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("......[]..........[]......")
            print("..........................")
            print("....||..............||....")
            print("....||..............||....")
            print("....||..............||....")
            print("....||..............||....")
            print("....==================....")
            print("..........................")
            break
        else:
            print("Returning to the main menu.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")