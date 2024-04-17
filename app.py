from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from utils.city_service import create_cities

load_dotenv()
api_key = os.getenv('OPEN_WEATHER_API_KEY')

app = Flask(__name__)
cities = create_cities(api_key)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # This will be implemented later to add new cities
        pass
    return render_template('index.html', cities=cities)


if __name__ == "__main__":
    app.run(debug=True)