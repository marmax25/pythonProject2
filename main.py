import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

# status = 'available'
# res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
#
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))


new_pet = {
    "id": 1596,
    "category": {
        "id": 10,
        "name": "kotik"
    },
    "name": "gorilla",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 26,
            "name": "popy"
        }
    ],
    "status": "available"
}

info_js = json.dumps(new_pet, ensure_ascii=False)

res = requests.post(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json'}, data=info_js)

print('Code (Add a new pet to the store) = ', res.status_code)
print('Response body (Add a new pet to the store):')
print(res.json())
print('Response headers (Add a new pet to the store):')
print(dict(res.headers))



