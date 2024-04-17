from flask import Flask, render_template, request
import requests
from models.city import City
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPEN_WEATHER_API_KEY')


cities = []
app = Flask(__name__)


def get_weather_info_by_coordinates(lat, lon):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}&units=imperial")
    weather_info = r.json()
    print(weather_info)
    weather_state = weather_info["weather"][0]["main"]
    temperature = weather_info["main"]["temp"]
    return weather_state, temperature


def add_cities():
    nyc_weather_state, nyc_temp = get_weather_info_by_coordinates("40.714272", "-74.005966")
    nyc = City.create_city("New York City", nyc_weather_state, nyc_temp)
    san_fran_weather_state, san_fran_temp = get_weather_info_by_coordinates("37.774929", "-122.419418")
    san_fran = City.create_city("San Francisco", san_fran_weather_state, san_fran_temp)
    houston_weather_state, houston_temp = get_weather_info_by_coordinates("29.763281", "-95.363274")
    houston = City.create_city("Houston", houston_weather_state, houston_temp)
    cities.extend([nyc, san_fran, houston])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    # this will be added later
    return render_template('index.html', cities=cities)


if __name__ == "__main__":
    add_cities()
    app.run(debug=True)