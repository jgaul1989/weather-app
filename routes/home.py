from models.city import City
from flask import Blueprint, render_template
from utils.db_utils import select_all_cities

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def index():
    cities = select_all_cities()
    return render_template("index.html", cities=cities)
