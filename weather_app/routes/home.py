from flask import Blueprint, render_template, request, redirect, url_for
from weather_app.utils.db_utils import select_all_cities, create_city, remove_city

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/crud', methods=['POST'])
def crud():
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    crud_action = request.form.get('crud-action')
    if crud_action == 'add':
        create_city(city, zipcode)
    elif crud_action == 'remove':
        remove_city(zipcode)
    return redirect(url_for('home.index'))


@home.route('/', methods=['GET'])
def index():
    cities = select_all_cities()
    return render_template('index.html', cities=cities)
