import requests
import json

def test_getPutUpdateUser():
    url = "https://reqres.in/api/users/2"
    payload = json.dumps({
    "name": "morpheus",
    "job": "zion resident"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)
