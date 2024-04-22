from weather_app.models.city import City
from .api_utils import get_weather_info_by_zip
from weather_app.extensions import db
from sqlalchemy.exc import IntegrityError
from flask import flash


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


def remove_city(zipcode):
    try:
        stmt = db.select(City).filter_by(zipcode=zipcode)
        result = db.session.execute(stmt)
        city = result.scalar_one_or_none()

        if city:
            db.session.delete(city)
            db.session.commit()
            flash('City successfully removed.', 'info')
        else:
            flash('City not found.', 'info')
    except Exception as e:
        flash(f'Something went wrong {e}', 'error')


def create_city(name, zipcode):
    state, temp, lat, lon = get_weather_info_by_zip(zipcode)
    if state and temp and lat and lon:
        try:
            city = City(city_name=name, weather_state=state, temp=temp, lat=lat, lon=lon, zipcode=zipcode)
            db.session.add(city)
            db.session.commit()
        except IntegrityError:
            print(f"{zipcode} already exists")
            flash("City already exists", "error")
            db.session.rollback()
            return False
        except Exception as e:
            print(f"Database error: {e}")
            flash("Database error", "error")
            db.session.rollback()
            return False
    else:
        return False
    return True


def select_all_cities():
    stmt = db.select(City).order_by(City.city_name)
    result = db.session.execute(stmt)
    cities = result.scalars().all()
    return cities
