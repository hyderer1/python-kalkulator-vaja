def calculator():
    history = []  # To store the history of calculations
    while True:
        print("\n--- Calculator ---")
        print("Select an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == '1':
                result = num1 + num2
                operation = "Addition"
            elif choice == '2':
                result = num1 - num2
                operation = "Subtraction"
            elif choice == '3':
                result = num1 * num2
                operation = "Multiplication"
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                    continue
                result = num1 / num2
                operation = "Division"

            # Format output with units
            print(f"Result of {operation} of {num1} and {num2} is: {result:.2f}")

            # Store the calculation in history
            history.append(f"{operation}: {num1} and {num2} = {result:.2f}")
            if len(history) > 3:
                history.pop(0)  # Keep only the last 3 calculations

            print("History of last 3 calculations:")
            for entry in history:
                print(entry)
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == '__main__':
    calculator()