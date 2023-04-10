def search_flights(fid, flights):
    flights_found = []

    for flight in flights:
        if flight['flight_id'] == fid:
            flights_found.append(flight)

    return flights_found


def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight["flight_id"] == fid:
            return i
    return -1