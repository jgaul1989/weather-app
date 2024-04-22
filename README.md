# Weather Application

## Introduction
This Weather Application is a Flask-based web service that allows users to get current weather information for different cities. It leverages the OpenWeatherMap API to fetch real-time weather data and display it in a user-friendly web interface.

## Features
- View current weather conditions for a list of cities.
- Add and remove cities from the watch list.
- Weather details include temperature, weather conditions, and more.

## Technologies Used
- **Python 3**: A powerful programming language used to build the backend.
- **Flask**: A web framework for Python used to create the web application.
- **SQLAlchemy**: ORM used for database interactions.
- **SQLite**: Database used to store city data.
- **Jinja2**: Templating language for Python, used to render the frontend.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip for installing dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-application.git
   cd weather-application
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Set up the environment variables:
   ```bash
   Modify the .env file to include your OpenWeatherMap API key, which is free
   on their website.

### Usage
- After launching the application, you can:
- View Weather: The homepage displays the current weather conditions for cities added to your watch list.
- Add a City: Use the form to add a new city by entering its name.
- Remove a City: Each city card has a delete button to remove the city from your watch list.
