# Day 10 /100 Python Revision
# Simple Calculator

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    
    while True:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations.get(operation_symbol)
        if calculation_function:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid operation! Try again.")
            continue

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        
        if choice == "y":
            num1 = answer
        else:
            calculator()  # Restart the calculator
            break

calculator()  # Start the calculator

