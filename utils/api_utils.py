import requests


def get_weather_info_by_coordinates(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return data["weather"][0]["main"], data["main"]["temp"]
