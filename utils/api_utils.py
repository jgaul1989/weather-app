import requests


def get_weather_info_by_coordinates(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data["weather"][0]["main"], data["main"]["temp"]


def get_weather_info_by_zip(zip_code, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data["weather"][0]["main"], data["main"]["temp"], data["coord"]["lat"], data["coord"]["lon"]


