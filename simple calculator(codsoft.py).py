# Simple Command-Line Calculator

# Step 1: Get input numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Show operation choices to the user
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Get the user's choice
choice = input("\nEnter your choice (1/2/3/4 or +, -, *, /): ")

# Step 4: Perform calculation based on choice
if choice == "1" or choice == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2" or choice == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3" or choice == "*":
    result = num1 * num2
    print(f"\nResult: {num1} × {num2} = {result}")

elif choice == "4" or choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} ÷ {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

else:
    print("\nInvalid choice. Please select a valid operation.")
