import requests

def test_getListUser():
    url = "https://reqres.in/api/users?page=2"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)