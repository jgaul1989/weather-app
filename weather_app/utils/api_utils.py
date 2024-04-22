import requests
from flask import flash


def get_weather_info_by_coordinates(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data["weather"][0]["main"], data["main"]["temp"]


def get_weather_info_by_zip(zip_code, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=imperial"
        response = requests.get(url)
        data = response.json()
        if data["weather"][0]["main"] and data["main"]["temp"] and data["coord"]["lat"] and data["coord"]["lon"]:
            return data["weather"][0]["main"], data["main"]["temp"], data["coord"]["lat"], data["coord"]["lon"]
        else:
            raise ValueError("Incomplete data received from weather service")
    except requests.exceptions.HTTPError as http_err:
        flash(f'An error occurred: {http_err}', "error")
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout:
        flash("Timeout occurred", "error")
        print("The request timed out")
    except requests.exceptions.RequestException as err:
        flash("There was an error while fetching weather information", "error")
        print(f"Request error occurred: {err}")
    except ValueError as ve:
        flash("Incomplete data received from weather service", "error")
        print(f"Value error: {ve}")
    return None


