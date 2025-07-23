def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero")
        return num1 / num2
    else:
        return "Invalid operation"

def save_to_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

def show_history():
    try:
        with open("history.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No history yet.")
            else:
                print("\n--- Calculation History ---")
                print(content)
    except FileNotFoundError:
        print("No history found.")

def main():
    print("Welcome to the Mini Calculator with History!")

    while True:
        print("\nOptions: +  -  *  /  |  'history' to view history  |  'q' to quit")
        operation = input("Enter an operation: ").strip()

        if operation == 'q':
            print("Goodbye!")
            break

        elif operation == 'history':
            show_history()
            continue

        if operation != ['+', '-', '*', '/']:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Try again.")
            continue

        result = calculate(num1, num2, operation)
        if isinstance(result, str):
            print(result)  # Show error message
        else:
            expression = f"{num1} {operation} {num2}"
            print(f"Result: {expression} = {result}")
            save_to_history(expression, result)

if __name__ == "__main__":
    main()


           
        
