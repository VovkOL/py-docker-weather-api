import os

import requests

API_KEY = os.getenv("WEATHER_API_KEY")
def get_weather() -> None:
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&aqi=no"
    res = requests.get(url)
    print(res.json())



if __name__ == "__main__":
    get_weather()
