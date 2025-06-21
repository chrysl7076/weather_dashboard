from flask import Flask, render_template, url_for

app = Flask(__name__)

cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai']

@app.route('/')
def index():
    city_data = []
    for i, city in enumerate(cities, start=1):
        data = {
            'name': city,
            'dashboard': url_for('static', filename=f'dashboard_{i}_{city}.png'),
            'forecast': url_for('static', filename=f'forecast_{i}_{city}.png')
        }
        city_data.append(data)
    return render_template('index.html', cities=city_data)

if __name__ == '__main__':
    app.run(debug=True)

