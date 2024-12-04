import art

# TODO 1 - Write the functions for the calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO 2 Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Todo 3 Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

total = 0


def calculator():
    print(art.logo)
    game = True
    total = None

    while game:
        if total is None:
            firstNumber = float(input("Welcome to the Calculator App, please type the first number:\n"))
        else:
            print(f"Using previous result: {total}")
            firstNumber = total

        symbol = input('Type a mathematical operator (a choice of "+", "-", "*", or "/"):\n')

        # Validate operator
        while symbol not in operations:
            print("Invalid operator. Please choose from '+', '-', '*', or '/'.")
            symbol = input('Type a mathematical operator (a choice of "+", "-", "*", or "/"):\n')

        secondNumber = float(input("Type the second number of your choice: \n"))

        result = int(operations[symbol](firstNumber, secondNumber))

        if result is not None:
            print(f"Result: {result}")
            total = result

        answer = input(
            "Do you want to continue working with the previous result? Type 'yes', 'no', or 'end':\n").lower()

        if answer == 'end':
            game = False
            print("Thank you for using the Calculator App. Goodbye!")

        if answer == 'no':
            calculator()
        if answer == 'yes':
            continue

calculator()
