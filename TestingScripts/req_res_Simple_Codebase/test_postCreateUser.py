import requests
import json

def test_postCreateUser():    
    url = "https://reqres.in/api/users"
    payload = json.dumps({
    "name": "morpheus",
    "job": "leader"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 201
    print(response.text)