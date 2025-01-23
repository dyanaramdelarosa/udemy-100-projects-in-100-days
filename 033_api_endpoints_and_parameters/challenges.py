import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.elapsed)
print(response.headers)

response.raise_for_status()
data =response.json()
print(data)
print(data["iss_position"]["longitude"])
