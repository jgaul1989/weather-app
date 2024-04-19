from flask import Blueprint, render_template, request, flash, redirect, url_for
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
        if not city or not zipcode:
            flash('City and zipcode are required!')
            return redirect(url_for('index'))
        if len(zipcode) != 5 or not zipcode.isdigit():
            flash('Zipcode must be five digits.')
            return redirect(url_for('index'))
        create_city(city, zipcode, api_key)
    cities = select_all_cities()
    return render_template("index.html", cities=cities)
