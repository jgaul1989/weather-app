import requests


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
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    return None


