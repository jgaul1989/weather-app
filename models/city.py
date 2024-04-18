
class City:
    def __init__(self, city_id, name, state, temp, lat, lon):
        self.city_id = city_id
        self.city_name = name
        self.weather_state = state
        self.temp = temp
        self.lat = lat
        self.lon = lon

    @classmethod
    def create_city(cls, city_id, name, state, temp, lat, lon):
        return cls(city_id, name, state, temp, lat, lon)