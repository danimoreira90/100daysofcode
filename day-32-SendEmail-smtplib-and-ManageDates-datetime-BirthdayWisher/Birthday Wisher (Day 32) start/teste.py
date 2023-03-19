# import smtplib
#
# """SMTP Information:
# Gmail host: smtp.gmail.com
# Hotmail host: smtp.live.com
# Yahoo host: smtp.mail.yahoo.com"""
#
#
# my_email = "dcm29031990@gmail.com"
# password = "tada3,5,6"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="dcm29031990@yahoo.com", msg="Hello")
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_week = now.weekday()
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=10, day=3, hour=7, minute=35)
print(date_of_birth)