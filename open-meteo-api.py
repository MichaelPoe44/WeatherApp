#import pandas as pd
import requests



'''
documentation

https://open-meteo.com/en/docs

'''



url = "https://api.open-meteo.com/v1/forecast"
param = {
    "latitude":53.43,
    "longitude":13.45,
    "hourly":"temperature_2m",      #an array of hourly parameters
    "temperature_unit":"fahrenheit"
}



response = requests.get(url=url, params=param)
if response.status_code != 200:
    print("bad get request")

else:
    response = response.json()





print(response["hourly_units"])



