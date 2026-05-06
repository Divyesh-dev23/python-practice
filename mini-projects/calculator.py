def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b!=0:
        return a/b
    else:
        return "Cannot divide by zero"
    
def multiply(a, b):
    return a*b

while True:

    op = input("Enter operation(+,-,*,/) or q to quit:-")

    if op.lower() == 'q':
        break
    if op not in ['+','-','*','/']:
        print("Invalid operator")
        print()
        continue

    try:
        a = float(input("Enter 1st value:-"))
        b = float(input("Enter 2nd value:-"))
    except ValueError:
        print("Invalid input")
        print()
        continue

    if op == '+':
        print(add(a,b))
    elif op == '-':
        print(subtract(a,b))
        print()
    elif op == '*':
        print(multiply(a,b))
        print()
    elif op == '/':
        print(divide(a,b))