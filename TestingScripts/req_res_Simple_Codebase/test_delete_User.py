import requests

def test_deleteUser():
    url = "https://reqres.in/api/users/250"
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 204
    print(response.text)