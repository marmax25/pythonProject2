from datetime import datetime, timezone
import arrow

base_url = 'https://petstore.swagger.io/v2'
headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}
headers2 = {'accept': 'application/json'}
headers3 = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

# Cоздание нового пользователя

new_user = {
    "id": 0,
    "username": "UserPet",
    "firstName": "Pety",
    "lastName": "Ivanov",
    "email": "kotik@mail.ru",
    "password": "123456",
    "phone": "+7950711",
    "userStatus": 0
}

# Добавление нового питомца

new_pet = {
    "id": 357,
    "category": {
        "id": 2,
        "name": "Barsik"
    },
    "name": "kotik",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 13,
            "name": "hor"
        }
    ],
    "status": "available"
}

# Изменение данных о питомце

update_new_pet = {
    "id": 357,
    "category": {
        "id": 2,
        "name": "string"
    },
    "name": "Kong",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 3,
            "name": "string"
        }
    ],
    "status": "sold"
}

