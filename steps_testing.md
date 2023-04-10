### How to test the app

Let's use pytest

`pip3 install pytest`

Create a tests folder

`mkdir tests`

Create the fixtures in a file called `conftest.py` inside the
`tests` folder:

```buildoutcfg
import pytest
from my_flights_api import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
```

Now we create a `test_app` file to test the app,
in the same directory `tests`.
Here we create the test:

```buildoutcfg
import json


def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'message': 'Welcome to the flights app'}
    assert expected == json.loads(res.get_data(as_text=True))
```

Create all your tests.

Lastly we call pytest

`python -m pytest`
