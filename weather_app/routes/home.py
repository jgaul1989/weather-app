from flask import Blueprint, render_template, request
from weather_app.utils.db_utils import select_all_cities, create_city
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_WEATHER_API_KEY')
home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        create_city(city, zipcode, api_key)
    cities = select_all_cities()
    return render_template("index.html", cities=cities)
