
class City:
    def __init__(self, name, state, temp, lat, lon):
        self.city_name = name
        self.weather_state = state
        self.temp = temp
        self.lat = lat
        self.lon = lon

    @classmethod
    def create_city(cls, name, state, temp, lat, lon):
        return cls(name, state, temp, lat, lon)