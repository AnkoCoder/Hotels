from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def countries():
    with open('db.json') as f:
        countries = json.load(f)
    return render_template('countries.html', countries=countries)


@app.route('/countries/<name>')
def country(name):
    with open('db.json') as f:
        countries = json.load(f)
        hotels = countries[name]
    return render_template('hotels.html', hotels=hotels)
