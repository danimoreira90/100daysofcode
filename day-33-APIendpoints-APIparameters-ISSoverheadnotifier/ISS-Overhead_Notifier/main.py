import requests
from datetime import datetime
import smtplib
import email.message
import time


msg = "Subject:Look Up!\n\nThe ISS is above you in the sky!"

MY_EMAIL = "dcm29031990@gmail.com"
MY_PASSWORD = "zaaktwnwyzonzybl"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        msg = email.message.Message()
        msg['Subject'] = "Look Up!"
        msg['From'] = MY_EMAIL
        msg['To'] = "dcm29031990@yahoo.com"
        password = MY_PASSWORD
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(msg)

        with smtplib.SMTP('smtp.gmail.com: 587') as connection:
            connection.starttls()
            # Login Credentials for sending the mail
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=msg['To'],
                                msg=msg
                                )
            print('Email enviado')

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



