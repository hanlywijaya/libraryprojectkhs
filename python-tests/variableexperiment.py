mark = int(input("Enter your mark out for SEN out of 100: "))

if mark > 100:
    print("Your mark is invalid.")
    (exit)

if mark < 50:
    print("You passed Software Engineering")
else:
    print("You failed Software Engineering")