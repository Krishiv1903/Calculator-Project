def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operation == "s":
        return a ** 2
    elif operation == "f":
        if a < 0 or not a.is_integer():
            return "Error: Enter a non-negative integer"
        result = 1
        for i in range(1, int(a) + 1):
            result *= i
        return result
    else:
        return "Invalid operation"

print("Welcome to the Simple Calculator!")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, s for square, f for factorial): ")

print("Calculation Result:", calculate(a, b, operation))