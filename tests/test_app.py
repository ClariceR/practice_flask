import json


def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'message': 'Welcome to the flights app'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_flights(app, client):
    del app
    res = client.get('/flights')
    assert res.status_code == 200
    expected = [
        {"from_city": "London",
         "to_city": "Helsinki",
         "days": [1, 3, 5, 7],
         "captain": {'name': 'Neil',
                     'surname': 'Bonn'},
         "duration_min": 92,
         "capacity": 100,
         "booked": 10,
         "available": 90,
         "flight_id": 555},

        {"from_city": "Manchester",
         "to_city": "Oslo",
         "days": [2, 4],
         "captain": {'name': 'Jorgen',
                     'surname': 'Kopff'},
         "duration_min": 55,
         "capacity": 80,
         "booked": 62,
         "available":  18,
         "flight_id": 1818},
    ]
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_flight_by_id(app, client):
    del app
    res = client.get('/flights/555')
    assert res.status_code == 200
    expected = [
        {"from_city": "London",
         "to_city": "Helsinki",
         "days": [1, 3, 5, 7],
         "captain": {'name': 'Neil',
                     'surname': 'Bonn'},
         "duration_min": 92,
         "capacity": 100,
         "booked": 10,
         "available": 90,
         "flight_id": 555}
    ]
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_flight_by_id_no_results(app, client):
    del app
    res = client.get('/flights/5589')
    assert res.status_code == 200
    expected = []
    assert expected == json.loads(res.get_data(as_text=True))
