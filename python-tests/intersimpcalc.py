number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))

print("Enter 1 for - operation")
print("Enter 2 for + operation")
print("Enter 3 for / operation")
print("Enter 4 for * operation")
operation = (input("Enter your operation: "))

if operation == "1":
    print("The answer is", number1 - number2)
elif operation == "2":
    print("The answer is", number1 + number2)
elif operation == "3":
    if number2 != 0:
        print("The answer is", number1 / number2)
    else:
        print("Cannot divide by zero")
elif operation == "4":
    print("The answer is", number1 * number2)
else:
    print("Invalid input")