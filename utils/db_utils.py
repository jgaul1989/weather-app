from models.city import City
from app import db


def create_default_cities():

    if City.query.first() is None:
        city_data = [
            (5128581, "New York City", "Cloudy", 57, 40.714272, -74.005966),
            (5391959, "San Francisco", "Sunny", 76, 37.774929, -122.419418),
            (4699066, "Houston", "Sunny", 80, 29.763281, -95.363274)
        ]
        for city_id, name, state, temp, lat, lon in city_data:
            city = City(city_id=city_id, city_name=name, weather_state=state, temp=temp, lat=lat, lon=lon)
            db.session.add(city)
        db.session.commit()


def select_all_cities():
    stmt = db.select(City).order_by(City.city_name)
    result = db.session.execute(stmt)
    cities = result.scalars().all()
    return cities
