from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_WEATHER_API_KEY')
flask_app = create_app()


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)