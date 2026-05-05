a = float(input("Enter 1st value:-"))
b = float(input("Enter 2nd value:-"))

op = input("Enter operation(+,-,*,/):-")

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
else:
    print("Invallid Operation\n")

