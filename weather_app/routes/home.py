from flask import Blueprint, render_template, request, redirect, url_for
from weather_app.utils.db_utils import select_all_cities, create_city
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_WEATHER_API_KEY')
home = Blueprint('home', __name__, template_folder='templates')


@home.route('/crud', methods=['POST'])
def crud():
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    crud_action = request.form.get('crud-action')
    if crud_action == 'add':
        create_city(city, zipcode, api_key)
    else:
        print('Hello World!!')
    return redirect(url_for('home.index'))


@home.route('/', methods=['GET'])
def index():
    cities = select_all_cities()
    return render_template('index.html', cities=cities)
