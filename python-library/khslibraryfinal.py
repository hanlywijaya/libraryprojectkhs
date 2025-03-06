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
        print("Invalid username or password, you have", attempts, "attempts left")
        attempts -=1
        if attempts ==0:
             print("You have run out of attempts. Please try again by rerunning the program.")
             exit()
        
print("1 - list all books")
print("2 - list of available book")
print("3 - borrow a book")
print("4 - return a book")
print("5 - exit")
operation = input("Please input an operation: ")

if operation == "1":
    print("**List of all books**")
    for bcode, book in bookdata.items():
        print(book, "-", bcode)