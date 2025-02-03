import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# print(response.elapsed)
# print(response.headers)
#
# response.raise_for_status()
# data =response.json()
# print(data)
# print(data["iss_position"]["longitude"])

MY_LAT = 37.058277
MY_LNG = -120.849915

parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(data)
print(f"{sunrise=}")
print(f"{sunset=}")

time_now = datetime.now()
print(f"{time_now.hour=}")
