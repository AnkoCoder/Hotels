from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def countries():
    with open('db.json') as f:
        countries = json.load(f)
        result = []
        for country in countries:
            result.append(
                { 
                    'name': country, 
                    'count': len(countries[country])
                }
            )
    return render_template('countries.html', countries=result)


@app.route('/countries/<name>')
def country(name):
    with open('db.json') as f:
        countries = json.load(f)
        hotels = countries[name]
    return render_template('hotels.html', hotels=hotels)
