# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

weight=int(input("weight :"))
height=float(input("Height :"))

"""
BMI FORMULA:

BMI = WEIGHT / (Height * Height)

"""

BMI = weight / (height * height)
print(int(BMI))