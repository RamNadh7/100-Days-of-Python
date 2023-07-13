##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from datetime import datetime
import pandas
import smtplib
import random

MY_EMAIL= "your_email"
PASSWORD= "Generated_Password"
"""
Generate the password from app passwords from google account settings security tab
"""
Letter_List=["letter_1.txt","letter_2.txt","letter_3.txt"]

now=datetime.now()
month=now.month
today=now.day
Today_Details=(month,today)

data=pandas.read_csv("birthdays.csv")

data_dict={(row_data.month,row_data.day) : row_data for  (index,row_data) in data.iterrows()}

if Today_Details in data_dict:
    letter_Type=random.choice(Letter_List)
    with open(f"./letter_templates/{letter_Type}") as letter:
        data=letter.read()
        temp=data_dict[Today_Details]
        print(temp)
        name=temp["name"]
        changed_data=data.replace("[NAME]",name)
        print(changed_data)

    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=temp["email"], msg=f"Subject:Happy Birthday\n{changed_data}") 