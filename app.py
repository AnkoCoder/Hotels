from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def countries():
    with open('db.json') as f:
        countries = json.load(f)
        countries = [
            { 
                'name': country, 
                'count': len(countries[country])
            } for country in countries
        ]
    return render_template('countries.html', countries=countries)


@app.route('/countries/<name>')
def country(name):
    with open('db.json') as f:
        countries = json.load(f)
        hotels = countries[name]
    return render_template('hotels.html', hotels=hotels)
