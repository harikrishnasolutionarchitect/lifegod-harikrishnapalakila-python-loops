print("Select the operation to perform   :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. division")

operation = input()

if operation == "1":
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    sum = int(n1) + int(n2)
    print("Sum of 2 numbers:", sum)
elif operation == "2":
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    sub = int(n1) - int(n2)
    print("Sub of 2 numbers:", sub)
elif operation == "3":
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    mul = int(n1) * int(n2)
    print("mul of 2 numbers:", mul)
elif operation == "4":
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    div = int(n1) / int(n2)
    print("div of 2 numbers:", div)
else:
    print("Invalid Entry")