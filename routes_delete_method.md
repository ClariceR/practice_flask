### How can we delete a flight?

*We will need the id of the flight we want to delete*

*We can then specify the method we want in our `route()` function like so:*

```buildoutcfg
@app.route('/flights/<int:fid>', method='DELETE')
```

*In order to remove the flight from the flights list, we can use `.pop()`*

*We can call our `get_index()` helper function in our function
that is triggered by the delete decorator*

```buildoutcfg
def delete_flight(fid):
    index_to_delete = get_index(fid, flights)
    flights.pop(flights[index_to_delete])
    
    return jsonify(flights)
```