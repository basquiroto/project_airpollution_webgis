# %%
from config import API_KEY 
import requests

# %%
api_key = API_KEY
lat = -28.684180668106055
lon = -49.36755496464967

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
weather_json = r.json()

# %%
city_temp = round(weather_json['main']['temp'] - 273.13, 2)