from models.city import City
from .api_utils import get_weather_info_by_coordinates, get_weather_info_by_zip


def create_cities(api_key):
    cities = []
    city_data = [
        ("New York City", "40.714272", "-74.005966"),
        ("San Francisco", "37.774929", "-122.419418"),
        ("Houston", "29.763281", "-95.363274")
    ]
    for name, lat, lon in city_data:
        state, temp = get_weather_info_by_coordinates(api_key, lat, lon)
        city = City.create_city(name, state, temp)
        cities.append(city)
    return cities


def add_city(name, zipcode, api_key):
    state, temp = get_weather_info_by_zip(zipcode, api_key)
    city = City.create_city(name, state, temp)
    return city
