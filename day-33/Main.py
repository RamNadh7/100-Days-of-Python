import requests
from datetime import datetime

LAT=17.389401
LNG=78.447177

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# data=response.json()
# # print(data)

# longitude=data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]

# iss_pos = (longitude,latitude)
# print(iss_pos)

parameters= {
    "lat": LAT,
    "lng": LNG,
    "formatted":0
}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise_time=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_time)
print(sunset_time)
time=datetime.now()
print(time.hour)