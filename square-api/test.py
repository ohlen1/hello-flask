from api import app
import json


def test_square():
    response = app.test_client().get("/square/100")
    square = json.loads(response.data.decode('utf-8')).get("result")
    assert square == 10000
