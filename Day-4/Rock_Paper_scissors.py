rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
usr_choice=int(input("welcome to the Game.\nWhat do you choose Type 0 for rock, 1 for paper and 2 for scissors "))

if usr_choice >=3:
    if usr_choice >=3:
        print("Your coice is invalid. You Lose!")

else:
    if usr_choice == 0:
        print("Your choice:\n\n")
        print(rock)
    elif usr_choice == 1:
        print("Your choice:\n\n")
        print(paper)
    else :
        print("Your choice:\n\n")
        print(scissors)



    com_choice=random.randint(0,2)

    if com_choice == 0:
        print("Computer choose:\n\n")
        print(rock)
    elif com_choice == 1:
        print("Computer choose:\n\n")
        print(paper)
    else:
        print("Computer choose:\n\n")
        print(scissors)




    if usr_choice == 0 and com_choice == 1:
      print("You Lose")
    elif usr_choice == 1 and com_choice == 2:
        print("You Lose")
    elif usr_choice == 2 and com_choice == 0:
        print("You Lose")
    elif usr_choice == com_choice:
        print("It's Draw")
    else:
        print("You Win")



