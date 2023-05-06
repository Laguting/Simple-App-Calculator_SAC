def calculator():
    # ask user to choose an operation
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4): ")

    # check if choice is valid
    try:
        choice = int(choice)
        if choice not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        calculator()

    # ask user for two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        calculator()

    # perform operation based on user's choice
    if choice == 1:
        result = num1 + num2
        operator = "+"
    elif choice == 2:
        result = num1 - num2
        operator = "-"
    elif choice == 3:
        result = num1 * num2
        operator = "*"
    elif choice == 4:
        try:
            result = num1 / num2
            operator = "/"
        except ZeroDivisionError:
            print("Cannot divide by zero. Please try again.")
            calculator()

    # display result
    print(f"{num1} {operator} {num2} = {result}")

    # ask user if they want to try again
    again = input("Do you want to try again? (y/n): ")
    if again.lower() == "y":
        calculator()
    else:
        print("Thank you!")

calculator()
