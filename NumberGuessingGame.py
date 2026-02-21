import random
print("You have to guess a number between 1-100")
cumputer_choice=random.randint(1,100)
attempt=1
while True:
    user_guess=int(input("Enter your guess (if you want to exit enter 0):"))
    if user_guess==0:
        print("Thank you!")
        break
    elif user_guess==cumputer_choice:
        print("Congratulation! You guess it right in",attempt,"attempt")
        break
    else:
        if user_guess>cumputer_choice:
            print("HINT: Guess it more low.")
            attempt+=1
        elif user_guess<cumputer_choice:
            print("HINT: Guess it more high")
            attempt+=1

        
