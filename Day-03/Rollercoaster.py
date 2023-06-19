print("welcome to Rollercoaster!!")

height=int(input("What's your height?"))

Bill = 0

if height>=120:
    print("You can ride the Rollercoaster!!")
    age=int(input("What's your age? "))
    if age<12:
        Bill=5
        print("Child ticket price is Rs. 5")
    elif age<=18:
        Bill = 7
        print("Youth ticket price is Rs. 7")
    elif age <=45 and age <=55:
        print("Enjoy the Free Ride. The ride is on us..")
    else:
        Bill = 12
        print("Adult ticket price is Rs.12")
    
    pic_bill = input("Do you want picture to be taken? Y or N.  ")
    if pic_bill == 'Y':
        Bill +=3

    print(f"Your final bill is {Bill}")
else:
    print("sorry,You need to grow taller to take this ride")