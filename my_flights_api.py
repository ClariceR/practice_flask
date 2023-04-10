from flask import Flask, jsonify
from flights_data import flights

app = Flask(__name__)


@app.route('/')
def welcome_message():
    return {'message': 'Welcome to the flights app'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)


if __name__ == '__main__':
    app.run()
