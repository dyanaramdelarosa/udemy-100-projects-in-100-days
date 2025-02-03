"""
Day 33 Project (API Endpoints and Parameters): ISS Overhead

This project sends an email notification whenever the ISS
is visible in their location
"""

import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LNG = -0.127758  # Your longitude
MY_EMAIL = "dyanaramdelarosa@gmail.com"
MY_PASSWD = "SAMPLE_PASSWD"


def get_iss_location() -> dict[str, float]:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    return {
        "lat": float(data["iss_position"]["latitude"]),
        "lng": float(data["iss_position"]["longitude"]),
    }


def is_iss_overhead() -> bool:
    iss_location = get_iss_location()
    print(f"Current ISS Location: {iss_location}")

    if abs(iss_location["lat"] - MY_LAT) > 5:
        return False
    if abs(iss_location["lng"] - MY_LNG) > 5:
        return False
    return True


def is_dark_now() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = datetime.now().hour

    if now_hour <= sunrise_hour or now_hour >= sunset_hour:
        return True
    return False


def send_email() -> None:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: ISS Overhead\nTake a look at the ISS now!"
    )


if __name__ == "__main__":

    while True:
        if not is_iss_overhead():
            print("ISS is far from your location.")
        elif not is_dark_now():
            print("It's too bright to see the ISS.")
        else:
            print("ISS is overhead! Check it now!")
            send_email()
        time.sleep(60)
