def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

a = int(input("First number: "))
b = int(input("Second number: "))

operation = 0

while True:
    action = input("What to do? (+ - * /):").lower().strip()
    
    if action == "+" or action == "add":
        print(f"Result: {add(a, b)}")
        operation += 1
    elif action == "-" or action == "subtract":
        print(f"Result: {subtract(a, b)}")
        operation += 1
    elif action == "*" or action == "multiply":
        print(f"Result: {multiply(a, b)}")
        operation += 1
    elif action == "/" or action == "divide":
        print(f"Result: {divide(a, b)}")
        operation += 1
    elif action in ["stop", "exit", "quit", "end"]:
        print(f"You did {operation} operations. Bye!")
        break
    else:
        print("I don`t know this action")