from flask import Flask
from flask import abort
from flask import render_template

import data

from work_with_data import sorted_hotels_by_price
from work_with_data import get_tours_by_departure


app = Flask(__name__)


@app.route('/')
def main():

    hotels_by_price = sorted_hotels_by_price(data.tours)

    return render_template("index.html", data=data, hotels_by_price=hotels_by_price)


@app.route('/departures/<departure>/')
def departures(departure):

    from_city = data.departures.get(departure)

    if from_city is None:
        abort(404)

    tours_by_departure = get_tours_by_departure(data, departure)

    return render_template("departure.html", data=data, departure=from_city, tours_by_departure=tours_by_departure)


@app.route('/tours/<int:id>/')
def tours(id):

    tour = data.tours.get(id)

    if tour is None:
        abort(404)

    departure = data.departures.get(tour["departure"])

    if departure is None:
        abort(404)

    return render_template("tour.html", data=data, tour=tour, departure=departure)


app.run(debug=True)
