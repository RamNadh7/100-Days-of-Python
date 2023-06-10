print("Welcome to the Tip Calculator")

Bill_Amount = float(input("What was the total Bill Amount? Rs. "))

Tip_Percentage = int(input("What percentage tip would you like to give? 10, 12, 15??  "))

Tip_Amount = (Tip_Percentage/100) * Bill_Amount

Bill_Split=int(input("How many people want to split? "))

Total_Bill = round((Tip_Amount+Bill_Amount)/Bill_Split,2)
Total_Bill="{:.2f}".format(Total_Bill)
print("Rs. " + str(Total_Bill))