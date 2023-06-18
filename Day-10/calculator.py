#Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {"+": add, 
"-": subtract, 
"*": multiply, 
"/": division
}


def calculator_function():
    print(logo)
    num1 = float(input("Enter the first number : "))

    for sym in operations:
        print(sym)

    should_continue = False
    while not should_continue:
        operation_sym = input("Choose the operation you want to perform: ")
        num2 = float(input("Enter ther next number :"))

        calculator = operations[operation_sym]
        result = calculator(num1, num2)

        print(f"{num1} {operation_sym} {num2} = {result}")

        if input(
                f"Type y to continue calculation with {result}, or type 'n' to start new calculation: "
        ).lower() == 'y':
            num1 = result
        else:
            should_continue = True
            calculator_function()


calculator_function()
