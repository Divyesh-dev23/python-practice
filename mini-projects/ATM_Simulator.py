balance = 10000

def deposit(balance , deposit_amount):
    balance += deposit_amount
    return balance

def withdraw(balance , withdraw_amount):
    balance -= withdraw_amount
    return balance

def show_menu():
    print("""
        1. DEPOSIT MONEY 
        2. WITHDRAW MONEY
        3. CHECK BALANCE
        4. QUIT
        """)

while True:
    show_menu()

    try:
        option = int(input("Enter option:- "))
    except ValueError:
        print("Invalid input")
        continue

    if option == 1:
        try:
            deposit_amount = float(input("Enter amount:- "))
            if deposit_amount <= 0:
                print("Enter valid amount")
                continue
            else:
                balance = deposit(balance,deposit_amount)
                print(f"Available Balance:- {balance}")
        except ValueError:
            print("Invalid input")
            continue
    elif option == 2:
        try:
            withdraw_amount = float(input("Enter amount:- "))
            if withdraw_amount <= 0:
                print("Enter valid amount")
                continue
            else:
                if withdraw_amount > balance:
                    print("Insufficient balance")
                    continue
                else:
                    balance = withdraw(balance,withdraw_amount)
                    print(f"Available Balance:- {balance}")
        except ValueError:
            print("Invalid input")
            continue
    elif option == 3:
        print(f"Available balance:- {balance}")
    elif option == 4:
        print("Thank you for using the ATM")
        break    

