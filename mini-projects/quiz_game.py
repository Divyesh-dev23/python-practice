print("This is a quiz game.\n")

print("you will be scored depending on the answers you give.\n")

quiz = {"Capital of India?":"delhi" , "2+2":"4" , "Total continents in this world?":"7" , 
             "Who is called the first citizen of INDIA?":"president"}

score = 0

for question , answer in quiz.items():

    print(question)

    ans = input("Answer:- ")

    if ans.lower() == answer:
        print("Correct answer!\n")
        score += 1
    else:
        print("Wrong answer.\n")
        print(f"Correct answer is:- {answer}")
    
print(f"Your total score is:- {score}")


