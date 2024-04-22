from flask import Flask
from weather_app.extensions import db


def create_app():
    app = Flask(__name__)
    app.secret_key = 'secretkey'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from utils.db_utils import create_default_cities
        db.create_all()
        create_default_cities()

    from routes.home import home
    app.register_blueprint(home)

    return app
