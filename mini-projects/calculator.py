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
        print(a+b)
        print()
    elif op == '-':
        print(a-b)
        print()
    elif op == '*':
        print(a*b)
        print()
    elif op == '/':
        if b!=0:
            print(a/b)
            print()
        else:
            print("Cannot divide by zero\n")
            continue

