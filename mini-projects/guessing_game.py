import random

print("The system had generated a random number between 1 to 10\n")

print("Guess the number and score a point\n")

print("NOTE :- You will have 3 chances\n")

chances = 3
points = 0

guess_gen = random.randint(1,10)

while (chances>0):
    try:
        guess_num = int(input(("Guess the number:- ")))

        if guess_num in range(1,11):
            if(guess_gen==guess_num):
                print("Correct guess\n")
                points += 1
                print("Guess the next random number\n")
                guess_gen = random.randint(1,10)
                continue
            else:
                chances -= 1
                if guess_num > guess_gen:
                    print("Too high")
                else:
                    print("Too low")
                print("Remaining chances:- ",chances)
        else:
            print("Enter number within range\n")
            continue
    except ValueError:
        print("Invalid input")
        chances -= 1
        print("Remaining chances:", chances)

print("Total points scored:- ", points)
        

    