
import random
from art import logo


EASY_LEVEL=10
HARD_LEVEL=5
def Num_Gen():
    return random.randint(1,100)

def guess(Generated_Num,opportunity):
    print(f"You have {opportunity} attempts remaining to guess the number.")
    while opportunity>0:
        if opportunity==1:
            opportunity-=1
            usr_guess=int(input("Make a Guess: "))
            if usr_guess==Generated_Num:
                result=f"You got it. The Result is {Generated_Num}"
                return result
            elif opportunity==0:
                return "You are run out of Guesses, You Lose."
            elif usr_guess<Generated_Num:
                print("Too Low")
            elif usr_guess>Generated_Num:
                print("Too High")

        else:
            usr_guess=int(input("Make a guess: "))
            opportunity-=1
            if usr_guess==Generated_Num:
                result=f"You got it. The Result is {Generated_Num}"
                return result
            elif usr_guess<Generated_Num:
                print("Too Low.")
                print("Guesss Again")
                print(f"You have {opportunity} attempts remaining to guess the number.")
            elif usr_guess>Generated_Num:
                print("Too High")
                print("Guess Again")
                print(f"You have {opportunity} attempts remaining to guess the number.")

       
print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thiniking of a number between 1 and 100")
Generated_Num=Num_Gen()
difficulty=input("Choose a difficulty. Type 'Easy' or 'Hard' : ").lower()
print(Generated_Num)


if difficulty == "easy" :
    print(guess(Generated_Num,EASY_LEVEL))
elif difficulty == "hard" :
    print(guess(Generated_Num,HARD_LEVEL))

