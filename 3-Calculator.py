# Simple Calculator

value1 = float(input("Enter first number: "))
value2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    print("Result:", value1 + value2)

elif choice == "2":
    print("Result:", value1 - value2)

elif choice == "3":
    print("Result:", value1 * value2)

elif choice == "4":
    if value2 != 0:
        print("Result:", value1 / value2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice! Please select a number between 1 and 4.")
    
