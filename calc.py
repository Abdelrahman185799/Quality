def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y


keys = ["+", "-", "*", "/"]

num1 = float(input("What's the first number?: "))


should_continue = True

while should_continue:

    num2 = float(input("What's the next number?: "))
    operation_symbol = input("Pick an operation: ")
    if operation_symbol not in keys:
        print("Wrong operation!")
        break
    if operation_symbol == "+":
        answer = add(num1, num2)
    if operation_symbol == "-":
        answer = subtract(num1, num2)
    if operation_symbol == "*":
        answer = multiply(num1, num2)
    if operation_symbol == "/":
        answer = divide(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
        num1 = answer
    else:
        should_continue = False
