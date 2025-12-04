import requests

header = { 'accept' : 'application/json' }

response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/4',headers= header)

print(response.status_code)
print(response.json())

assert response.status_code == 200, 'Fail'
print('pass')
