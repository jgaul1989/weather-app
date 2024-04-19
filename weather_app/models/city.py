from sqlalchemy.orm import Mapped, mapped_column
from weather_app.extensions import db


class City(db.Model):
    __tablename__ = 'city'
    city_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    city_name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    weather_state: Mapped[str] = mapped_column(db.String(50))
    temp: Mapped[float] = mapped_column(db.Float)
    lat: Mapped[float] = mapped_column(db.Float)
    lon: Mapped[float] = mapped_column(db.Float)
    zipcode: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"City {self.city_name}"