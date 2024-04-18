from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from routes.home import home
    app.register_blueprint(home)

    with app.app_context():
        from utils.db_utils import create_default_cities
        from models.city import City
        db.create_all()
        create_default_cities()
    return app
