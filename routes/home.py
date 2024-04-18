from models.city import City
from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World!"
