print("Ensure to enter a mark between 0 and 100.")
print(".")
print(".")
print(".")
print(".")
print(".")
mark1 = int(input("Enter mark 1: "))
if mark1 < 0 or mark1 > 100:
    print("Mark 1 is invalid. Please open the program again and input a mark between 0 and 100.")
    exit()
subject1 = (input("Enter subject 1: "))
mark2 = int(input("Enter mark 2: "))
if mark2 < 0 or mark2 > 100:
    print("Mark 2 is invalid. Please open the program again and input a mark between 0 and 100.")
    exit()
subject2 = (input("Enter subject 2: "))
mark3 = int(input("Enter mark 3: "))
if mark3 < 0 or mark3 > 100:
    print("Mark 3 is invalid. Please open the program again and input a mark between 0 and 100.")
    exit()
subject3 = (input("Enter subject 3: "))

if mark1 < 50:
    print("You failed", (subject1))
else:
    print("You passed", (subject1))
    
if mark2 < 50:
    print("You failed", (subject2))
else:
    print("You passed", (subject2))

if mark3 < 50:
    print("You failed", (subject3))
else:
    print("You passed", (subject3))