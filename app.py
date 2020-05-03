from flask import Flask, render_template, request
from sqlalchemy import func
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'something'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin = Admin(app, name='hotels')
db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(400), unique=True, nullable=False)
    photo = db.Column(db.String(1000), nullable=False)
    items = db.relationship('Hotel', backref='country')

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(400), unique=True, nullable=False)
    photo = db.Column(db.String(1000), nullable=False)
    booking_page = db.Column(db.String(400), nullable=False)


# Отображение колонок, которые необходимо видеть в админке
class CountryAdmin(ModelView):
    column_list=['id', 'name']

class HotelAdmin(ModelView):
    column_list=['id', 'name', 'country_id', 'stars']


admin.add_view(CountryAdmin(Country, db.session))
admin.add_view(HotelAdmin(Hotel, db.session))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/countries')
def country():
    search = request.args.get('search')
    if search:
        countries = Country.query.filter(func.lower(Country.name).contains(search)).all()
    else:
        countries = Country.query.all()
    return render_template('countries.html', countries=countries, search=search)


# @app.route('/countries/<name>')
# def country_search(name):
#     selected_country = Country.query.get(Country.name)
#     return render_template('countries.html', selected_country=selected_country)


@app.route('/hotels')
def hotels():
    stars = request.args.getlist('stars')
    print(request.args)
    if stars:
        stars = [int(star) for star in stars]
        hotels = Hotel.query.filter(Hotel.stars.in_(stars)).all()
    else:
        hotels = Hotel.query.all()
    return render_template('hotels.html', hotels=hotels, stars=stars)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
