# Basic Calculator Program
def calculator():
    print("\n🖩 Basic Calculator 🖩")
    print("----------------------")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform the calculation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Invalid operator! Please use +, -, *, or /.")
            return

        # Display result
        print(f"\nResult: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
calculator()
