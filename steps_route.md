## How to setup the Flask routes file

First, we need to import the Flask class and jsonify function from flask:

`from flask import Flask, jsonify`

We also need to import the functions from utils

`from utils import search_flight`

And for now we need the dummy data we created

`from flights_data import flights`

Next, we need create an instance of the Flask class

`app = Flask(__name__)`

Now we are ready to create the first route.
We start by creating the route decorator:

```buildoutcfg
@app.route('/flights')
```

The decorator will tell Flask what URL will trigger the function we create next:

```buildoutcfg
def get_flights():
    return jsonify(flights)
```

This is how it looks:
```buildoutcfg
@app.route('/flights')
def get_flights():
    return jsonify(flights)
```

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

We finish by adding this to the end of the file:
```buildoutcfg
if __name__ == '__main__':
    app.run(debug=True)
```
The run() function runs the application with our local server.



as we all know 😉 `if __name__ == '__main__':`  ensures that the server only runs our app if the script is executed directly from the Python Interpreter.

If we use it as an imported module (for example when we get to test it), then the script won't run, and that's exactly what we want.

When we run our app, we can see it in our local server.

