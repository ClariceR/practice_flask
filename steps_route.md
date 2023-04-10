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

`@app.route('/')`

The decorator will tell Flask what URL will trigger the function we create next:
```buildoutcfg
def welcome_message():
    return {'message': 'Welcome to the flights app'}
```

Here is how it looks:

```buildoutcfg
@app.route('/')
def welcome_message():
    return {'message': 'Welcome to the flights app'}
```

[> GET method routes](/routes_get_method.md)

[> DELETE method route](/routes_delete_method.md)

We finish by adding this to the end of the file:
```buildoutcfg
if __name__ == '__main__':
    app.run(debug=True)
```
The run() function runs the application with our local server.



as we all know 😉 `if __name__ == '__main__':`  ensures that the server only runs our app if the script is executed directly from the Python Interpreter.

If we use it as an imported module (for example when we get to test it), then the script won't run, and that's exactly what we want.

When we run our app, we can see it in our local server.

