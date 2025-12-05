import requests
import json

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

header = {
    'accept' : 'text/plain',
    'content-type' : 'application/json'
}

request_payload = {"id": 150,
  "title": "Vilva",
  "dueDate": "2025-12-05T17:55:09.328Z",
  "completed": True
}

response = requests.post(url,headers = header,json = request_payload)

print(response.status_code)
print(response.text)
data = response.json()

assert response.status_code == 200 , 'fail'
print('OK')
assert data['id'] == 150 , 'wrong id value'
print(f'id value is {data['id']}')
