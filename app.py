from flask import Flask, render_template, request

app = Flask(__name__)
cities = ['New York', 'San Francisco', 'Los Angeles']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        cities.append(new_city)
    return render_template('index.html', cities=cities)


if __name__ == "__main__":
    app.run(debug=True)