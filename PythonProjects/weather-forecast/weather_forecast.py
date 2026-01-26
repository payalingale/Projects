import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

api_key = os.environ.get('api_key')
api_url = 'https://api.openweathermap.org/data/2.5/weather'


def getCityWeather(cityName,units='metric'):
  try:
   weatherData={}
   weatherForeCast={}
   param = {'q':cityName,'appid':api_key,'units':units}
   response = requests.get(api_url,params=param)
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


#STEP 1: Display Weather Nicely (10 minutes)
#Add this function below your getCityWeather function:
def displayCityWeather(weather_data,city_name):
 
 if not weather_data or 'error' in weather_data:
  return {'City weather details not found'}

 sunrise_time = datetime.fromtimestamp(weather_data['sunrise_time']).strftime('%H:%M')
 sunset_time = datetime.fromtimestamp(weather_data['sunset_time']).strftime('%H:%M')

     # Get wind direction
 wind_deg = weather_data['wind_direction']
 directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
 wind_dir = directions[round(wind_deg / 45) % 8]
 
 #display
 print(f'-'*50)
 print(f'City is {city_name.upper()}')
 print(f'Temperature of {city_name} is {weather_data['temp']}')
 print(f'It feels like {weather_data['weather_desc']}')
 print(f'Wind direction is {wind_dir}')
 print(f'Sunrise will be at {sunrise_time}')
 print(f'Sunset will be at {sunset_time}')

def getWeatherForecast():
      """Get 5-day weather forecast"""
      pass

def getWeatherHistory():
      """Get weather history"""
      pass

#🔹 STEP 2: Add Menu System (10 minutes)
def show_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("🌤️  WEATHER DASHBOARD")
    print("=" * 50)
    print("1. Current Weather")
    print("2. 5-Day Forecast")
    print("3. Weather History")
    print("4. Exit")
    print("=" * 50) 

def main():
   """Main program loop"""
   if not api_key:
    return {'api_key not found'}
print("✅ API key loaded!")
while True:
  show_menu()
  choice = input('Choose from (1 - 4)').strip()
  if choice == 1:
    getCityWeather('dubai')
  elif choice == 2:
   getWeatherForecast()
  elif choice == 3:
    getWeatherHistory()
  elif choice == 4:
    print('GoodBye')
    break
  else:
    print('Invalid choice')



  


city = 'dubai'
weather_data = getCityWeather(city)
displayCityWeather(weather_data,city)
