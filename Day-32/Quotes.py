import smtplib
import datetime as dt
import random

MY_EMAIL= "ramanadh99@gmail.com"
PASSWORD= "cdkjgekexaydlesm"


now=dt.datetime.now()
day_of_week=now.weekday()
# print(day_of_week)
if day_of_week==0:
    with open("quotes.txt") as quote_file:
        quote_data_list=quote_file.readlines()
        #print(data)
    
    
    Today_quote=random.choice(quote_data_list)

    #connection = smtplib.SMTP("smtp.gmail.com")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="raviraj1998a@gmail.com", msg=f"Subject:Mondays Motivation\n{Today_quote}")
        
        #As we used the With methd to create conection need not to close it manually just like file open method
        #connection.close()
