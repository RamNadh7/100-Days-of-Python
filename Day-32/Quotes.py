import smtplib
import datetime as dt
import random

MY_EMAIL= "Your Maild ID"
PASSWORD= "Generated Password"
"""
Generate the password from app passwords from google account settings security tab

"""

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
        """
Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com
"""
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="To Mail Id", msg=f"Subject:Mondays Motivation\n{Today_quote}")
        
        #As we used the With methd to create conection need not to close it manually just like file open method
        #connection.close()