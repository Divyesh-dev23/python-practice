import random

print("Play rock_paper_scissors with the system\n")

print("Your score will be calculated\n")

score = 0
score_c = 0

choices = ["rock","paper","scissors"]

while True:
    user = input("Enter your choice:- ").lower()
    computer = random.choice(choices)

    if user == 'q':
        break
    
    if user not in choices:
        print("Invalid input\n")
        continue

    print("Computer choice:- ",computer)
    print()

    if computer == user:
        print("Draw")
    elif ((user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper")):
        print("You win")
        score += 1
    else:
        print("Computer wins")
        score_c += 1
    
print("Your total score:- ",score)
print("Computer total score:- ",score_c)





