import time

userdata = {
    'sgilmore' : 'Pass1',
    'bwiseman' : 'Pass2',
    'uhalaj' : 'Pass3',
    'qwang' : 'Pass4',
    'mkassar' : 'Pass5',
    'adib' : 'Pass6',
    'bwiseman' : 'Pass7',
    'kjohnson' : 'Pass8',
    'fjose' : 'Pass9',
    'mmansour' : 'Pass10',
}

namedata = {
    'sgilmore' : 'Sam Gilmore',
    'bwiseman' : 'Bella Wiseman',
    'uhalaj' : 'Umar Halaj',
    'qwang' : 'Qing Wang',
    'mkassar' : 'Maryam Kassar',
    'adib' : 'Ali Dib',
    'bwiseman' : 'Benji Wiseman',
    'kjohnson' : 'Khadija Johnson',
    'fjose' : 'Fiona Jose',
    'mmansour' : 'Mathew Mansour',
}

bookdata = {
        '1101' : 'In Search of Lost Time',
        '1102' : 'Ulysses',
        '1103' : 'Don Quixote',
        '1104' : 'The Great Gatsby',
        '1105' : 'Moby Dick',
        '1106' : 'One Hundred Years of Solitude',
        '1107' : 'War and Piece',
        '1108' : 'Hamlet',
        '1109' : 'Lolita',
        '1110' : 'The Odyssey',
        '1111' : 'The Brothers Karamazov',
        '1112' : 'The Adventures of Huckleberry Finn',
        '1113' : 'Madame Bovary',
        '1114' : 'The Catcher in the Rye',
        '1115' : 'The Divine Comedy'
}

bookavailability = {
        '1101' : 'T',
        '1102' : 'T',
        '1103' : 'T',
        '1104' : 'F',
        '1105' : 'F',
        '1106' : 'T',
        '1107' : 'F',
        '1108' : 'F',
        '1109' : 'T',
        '1110' : 'T',
        '1111' : 'F',
        '1112' : 'F',
        '1113' : 'T',
        '1114' : 'T',
        '1115' : 'F',
}

print("Welcome to Kingsgrove High School's library system")
attempts = 3
while attempts > 0:
    Username = input("Please input username: ")
    Password = input("Please input password: ")
    if Username in userdata and userdata[Username] == Password:
        print("Welcome", namedata[Username])
        break
    else:
        if attempts > 0:
            attempts -=1
            print("\n"*2)
            print("Invalid username or password, you have", attempts, "attempts left")
        if attempts ==0:
            print("\n"*2)
            print("You have run out of attempts. Please try again by rerunning the program.")
            exit()

while True:
    print("\n"*15)
    print("Welcome to Kingsgrove High School's library system", namedata[Username])
    print("1 - List all books")
    print("2 - List of available books")
    print("3 - Borrow a book")
    print("4 - Return a book")
    print("5 - Exit library")
    print("\n"*2)
    operation = input("Please input an function number: ")

    if operation == "1":
        print("**List of all books**")
        index = 0
        for bcode, book in bookdata.items():
            print(index,".", book, "-", bcode)
            index +=1

    elif operation == "2":
        print("**List of all available books**")
        index = 0
        for bcode, book in bookdata.items():
            if bookavailability[bcode] == "T":
                print(index,".", book, "-", bcode)
                index +=1
        print("Resting for 5 seconds before returning to function menu...")
        time.sleep(5)

    elif operation == "3":
        print("**List of all available books**")
        index = 0
        for bcode, book in bookdata.items():
            if bookavailability[bcode] == "T":
                print(index,".", book, "-", bcode)
                index +=1
        borrowinput = input("Please input the book code you would like to borrow: ")
        if borrowinput in bookdata and bookavailability[borrowinput] == "T":
            print("You have requested for", "'",bookdata[borrowinput],"' to be borrowed.")
        else:
            print("Unavailable book or invalid book code. Please try again later.")
    
    elif operation == "4":
        print("**List of all available books**")
        index = 0
        for bcode, book in bookdata.items():
            if bookavailability[bcode] == "F":
                print(index,".", book, "-", bcode)
                index +=1
        borrowinput = input("Please input the book code you would like to return: ")
        if borrowinput in bookdata and bookavailability[borrowinput] == "F":
            print("You have requested for", "'",bookdata[borrowinput],"' to be returned.")
        else:
            print("Incorrect book or invalid book code. Please try again later.")

    elif operation == "5":
        print("\n"*2)
        exitconfirmation = input("Are you sure you want to exit? (y/n): ")
    if exitconfirmation == "y":
        print("Thank you for using Kingsgrove High School's library services, {}!".format(namedata[Username]))
        print("Developed by Hanly Wijaya, 2025")
        print("All rights reserved, 2025 HANLY WIJAYA ©")
        print("\n"*2)
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
        continue
    
else:
    print("Invalid function number. Please try again.")