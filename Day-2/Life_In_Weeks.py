# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = int(input("What's you age?\n"))

rem_age = (90 - age)
Months= rem_age* 12

Weeks = rem_age * 52

Days = rem_age * 365

print(f"You have {Days} days, {Weeks} weeks, and {Months} months")