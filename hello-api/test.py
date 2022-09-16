from api import app
from api import set_previous_name
import json


def test_hello():
    response = app.test_client().get('/hello')
    res = json.loads(response.data.decode('utf-8')).get("message")

    assert response.status_code == 200
    assert res == 'Hello world'

def test_hello_with_input_name():
    response = app.test_client().get('/hello?name=John')
    res = json.loads(response.data.decode('utf-8')).get("message")

    assert response.status_code == 200
    assert res == 'Hello John'

def test_set_input_name():
    response = app.test_client().post("/hello", json={"name": "John"})
    assert response.status_code == 200


def test_hello_with_cached_name():
    set_previous_name("John")
    response = app.test_client().get('/hello')
    res = json.loads(response.data.decode('utf-8')).get("message")
    assert res == 'Hello John'


def test_hello_with_cached_name_and_input_name():
    set_previous_name("John")
    response = app.test_client().get('/hello?name=Johnny')
    res = json.loads(response.data.decode('utf-8')).get("message")
    assert res == 'Hello Johnny, previously known as John'
