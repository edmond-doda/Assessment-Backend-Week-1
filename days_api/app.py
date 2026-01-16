"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)


app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


def clear_history():
    """Clears the app history."""
    app_history.clear()


@app.get("/")
def index():
    """Returns an API welcome message."""
    return jsonify({"message": "Welcome to the Days API."})


@app.post('/between')
def finds_dates_between():
    """Returns the number of days between two dates"""
    add_to_history(request)
    data = request.json

    if not data:
        return {"error": "Request body required"}, 400

    first_date = convert_to_datetime(data['first'])
    last_date = convert_to_datetime(data['last'])
    days = get_days_between(first_date, last_date)

    return {"days": days}, 201


@app.post('/weekday')
def finds_weekday():
    """Returns the weekday of a date"""
    add_to_history(request)
    data = request.json

    if not data:
        return {"error": "Request body required"}, 400

    date_object = convert_to_datetime(data['date'])
    day = get_day_of_week_on(date_object)

    return {"weekday": day}, 201


@app.get('/history')
def get_history():
    """Returns details on the last x amount of requests"""
    args = request.args.to_dict()
    number = args.get("number")

    if not number:
        number = 5

    if (number < 1) or (number > 20):
        return {"error": "Number must be between 1 and 20"}, 400

    return app_history[-number:], 200


@app.delete('/history')
def delete_history():
    clear_history()
    return {"status": "History cleared"}, 200


@app.get("/current_age")
def get_age():
    add_to_history(request)
    data = request.json
    if not data['date']:
        return {"error": "Request body must contain 'date'"}, 400

    date_object = convert_to_datetime(data['date'])
    age = get_current_age(date_object)

    return {'current age': age}, 200


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(port=8080, debug=True)
