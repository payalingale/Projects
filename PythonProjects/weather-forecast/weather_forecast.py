import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('api_key')
api_url = 'https://api.openweathermap.org/data/2.5/weather'


def getCityWeather(cityName,units):
  try:
   weatherData={}
   weatherForeCast={}
   param = {'q':cityName,'appid':api_key,'units':units}
   response = requests.post(api_url,params=param)
   weatherData = response.json()
   if (response.status_code == 200):
    weatherForeCast = {
    'temp':weatherData['main']['temp'],
    'feels_like':weatherData['main']['feels_like'],
    'weather_desc':weatherData['weather'][0]['description'],
    'humidity_percent':weatherData['main']['humidity'],
    'wind_speed':weatherData['wind']['speed'],
    'wind_direction':weatherData['wind']['deg'],
    'sunrise_time':weatherData ['sys']['sunrise'],
    'sunset_time':weatherData ['sys']['sunset']
    }
    return weatherForeCast
   else:
    print(response.status_code)
  except Exception as e:
   return {f'error as str{e}'}

  


print(getCityWeather('dubai','metric'))
