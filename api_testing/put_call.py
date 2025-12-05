import requests
import json

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/15'

header_get = {
    'accept' : 'text/plain',
'Content-Type' : 'application/json'
}

print("before update")

response = requests.get(url,headers = header_get)
print(response.json())

header_put = {
    'accept' : 'text/plain',
'Content-Type' : 'application/json'
}

putpayload = {
  "id": 20,
  "title": "string no: 20",
  "dueDate": "2025-12-05T19:19:50.228Z",
  "completed": True
}

print("after update")

response_put = requests.put(url,headers = header_put, json = putpayload)
print(response_put.json())