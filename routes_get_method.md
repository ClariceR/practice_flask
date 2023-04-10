### Creating our routes and using the proper methods

When we don't specify the method, the default is GET:

*Get all flights:*

```buildoutcfg
@app.route('/flights')
def get_flights():
    return jsonify(flights)
```

*Get a specific flight*

In order to search for a specific flight, we need:
1. the flight id
2. the function we created in the utils folder

This is how we add the id to the route as a variable:

i. We add the variable inside < >

ii. It's good practice to explicitly specify the type of the variable:

*type:variable*

```buildoutcfg
@app.route('/flights/<int:fid>')
```
Then the function to be triggered:
```buildoutcfg
def get_flight(fid):
    return jsonify(search_flight(fid, flights))
```

Together:
```buildoutcfg
@app.route('/flights/<int:fid>')
def get_flight_by_id(fid):
    return jsonify(search_flight(fid, flights))
```

> Note that we pass only the `fid` to the `get_flight_by_id` function,
> as that's the parameter that comes from the url in the decorator.
> Also, if we called the variable `fid` in the url, we need to pass it as `fid`
> to the function below, and to the helper function.
> It has to be the same name, or it won't work.
>
> If we pass `flights` as well, it won't work.