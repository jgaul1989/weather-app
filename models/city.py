
class City:
    def __init__(self, name, state, temp):
        self.city_name = name
        self.weather_state = state
        self.temp = temp

    @classmethod
    def create_city(cls, name, state, temp):
        return cls(name, state, temp)