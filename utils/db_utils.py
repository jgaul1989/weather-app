from models.city import City
from .api_utils import get_weather_info_by_zip
from app import db


def create_default_cities():

    if City.query.first() is None:
        city_data = [
            ("New York City", "Cloudy", 57, 40.714272, -74.005966, "10001"),
            ("San Francisco", "Sunny", 76, 37.774929, -122.419418, "94016"),
            ("Houston", "Sunny", 80, 29.763281, -95.363274, "77001")
        ]
        for name, state, temp, lat, lon, zipcode in city_data:
            city = City(city_name=name, weather_state=state, temp=temp, lat=lat, lon=lon, zipcode=zipcode)
            db.session.add(city)
        db.session.commit()


def create_city(name, zipcode, api_key):
    state, temp, lat, lon = get_weather_info_by_zip(zipcode, api_key)
    city = City(city_name=name, weather_state=state, temp=temp, lat=lat, lon=lon, zipcode=zipcode)
    db.session.add(city)
    db.session.commit()


def select_all_cities():
    stmt = db.select(City).order_by(City.city_name)
    result = db.session.execute(stmt)
    cities = result.scalars().all()
    return cities
