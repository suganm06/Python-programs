score = 0
i = 1 

print("Are you ready to play? (yes/no): ")
ready = input().strip().lower()

if ready == 'yes':
    print("\nRules of the quiz:")
    print("1. You will be asked 5 questions.")
    print("2. Answer with 'yes' or 'no'.")
    print("3. You get +1 point for a correct answer.")
    print("4. You get -1 point for a wrong answer.")
    print("5. Your score will be shown at the end.\n")
    while i <= 5:
        if i == 1:
            print(i,": Is Python a programming language? (yes/no): ")
            answer = input().strip().lower()
            if answer == 'yes':
                score += 1
                print("WOW! Correct answer")
            else:
                score -= 1
                print("OOPS! Wrong answer")
        elif i == 2:
            print(i,": Is Earth the fourth planet from the Sun? (yes/no): ")
            answer = input().strip().lower()
            if answer == 'no':
                score += 1
                print("WOW! Correct answer")
            else:
                score -= 1
                print("OOPS! Wrong answer")
        elif i == 3:
            print(i,": Is 10 + 5 equal to 15? (yes/no): ")
            answer = input().strip().lower()
            if answer == 'yes':
                score += 1
                print("WOW! Correct answer")
            else:
                score -= 1
                print("OOPS! Wrong answer")
        elif i == 4:
            print(i,": Is the capital of Japan Beijing? (yes/no): ")
            answer = input().strip().lower()
            if answer == 'no':
                score += 1
                print("WOW! Correct answer")
            else:
                score -= 1
                print("OOPS! Wrong answer")
        elif i == 5:
            print(i,": Does water boil at 90°C at sea level? (yes/no): ")
            answer = input().strip().lower()
            if answer == 'no':
                score += 1
                print("WOW! Correct answer")
            else:
                score -= 1
                print("OOPS! Wrong answer")
        
        i += 1

    print(f"Your final score is:",score)
    if(score<3):
        print("Better luck next time")
    elif(score<=4):
        print("Good score")
    else:
        print("perfect score")        
    
else:
    print("Maybe next time!")
