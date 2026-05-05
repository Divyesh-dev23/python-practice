while True:
    a = float(input("Enter 1st value:-"))
    b = float(input("Enter 2nd value:-"))

    op = input("Enter operation(+,-,*,/) or q to quit:-")

    if op == 'q':
        break

    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        if b!=0:
            print(a/b)
        else:
            print("Cannot divide by zero\n")
    else:
        print("Invallid Operation\n")

