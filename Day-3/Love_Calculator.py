"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
L_count=name1.count("l")+name2.count("l")
O_count=name1.count("o")+name2.count("o")
V_count=name1.count("v")+name2.count("v")
E_count=name1.count("e")+name2.count("e")

t_count=name1.count("t")+name2.count("t")
R_count=name1.count("r")+name2.count("r")
U_count=name1.count("u")+name2.count("u")
EE_count=name1.count("e")+name2.count("e")

First_count=str(t_count+R_count+U_count+EE_count)
second_count=str(L_count+O_count+V_count+E_count)
total_count=int(First_count+second_count)

if(total_count<10 or total_count>90):
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count>40 and total_count<50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
