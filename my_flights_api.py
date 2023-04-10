from flask import Flask, jsonify
from flights_data import flights
from utils import search_flights, get_index

app = Flask(__name__)


@app.route('/')
def welcome_message():
    return {'message': 'Welcome to the flights app'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)


@app.route('/flights/<int:fid>')
def get_flight_by_id(fid):
    return jsonify(search_flights(fid, flights))


@app.route('/flights/<int:fid>', methods=['DELETE'])
def delete_flight(fid):
    index_to_delete = get_index(fid, flights)
    flights.pop(flights[index_to_delete])
    return jsonify(flights)


if __name__ == '__main__':
    app.run()
