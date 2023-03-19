import smtplib
import email.message
import datetime as dt
import random

MY_EMAIL = "dcm29031990"
MY_PASSWORD = "zaaktwnwyzonzybl"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    msg = email.message.Message()
    msg['Subject'] = "Monday Motivation"
    msg['From'] = MY_EMAIL
    msg['To'] = 'dcm29031990@yahoo.com'
    password = MY_PASSWORD
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(quote)

    with smtplib.SMTP('smtp.gmail.com: 587') as connection:
        connection.starttls()
        # Login Credentials for sending the mail
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=msg['To'],
                            msg= msg.as_string().encode('utf-8'))
        print('Email enviado')

