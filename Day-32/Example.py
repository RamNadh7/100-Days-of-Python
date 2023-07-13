# import smtplib

# my_email= "Your mail id"
# password= "Generated password"
"""
Generate the password from app passwords from google account settings security tab
"""

# connection = smtplib.SMTP("smtp.gmail.com")

"""
Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com
"""

# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs="To_mail address", msg="Subject:Test\nsent through python code")
# connection.close()


import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
print(year,month)

day_of_week=now.weekday()
print(day_of_week)

DOB=dt.datetime(year=1990, month=4,day=1,hour=4)
print(DOB)