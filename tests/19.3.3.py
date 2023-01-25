import requests
import json
from config import new_user, base_url, headers1, headers2, headers3, new_pet, update_new_pet

# Добавить нового питомца

info_js = json.dumps(new_pet, ensure_ascii=False)

res = requests.post(f'{base_url}/pet', headers=headers1, data=info_js)

print('Code (Add a new pet to the store) = ', res.status_code)
print('Response body (Add a new pet to the store):')
print(res.json())
print('Response headers (Add a new pet to the store):')
print(dict(res.headers))

# Изменения данных о питомце

info_js = json.dumps(update_new_pet, ensure_ascii=False)

res = requests.put(f'{base_url}/pet', headers=headers1, data=info_js)

print('Code (Update an existing pet) = ', res.status_code)
print('Response body (Update an existing pet):')
print(res.json())
print('Response headers (Update an existing pet):')
print(dict(res.headers))

# Удалить питомца

res = requests.delete(f'{base_url}/pet/{new_pet}', headers=headers2)

print('Code (Delete a pet)= ', res.status_code)
print('Response body (Delete a pet):')
print(res.json())
print('Response headers (Delete a pet):')
print(dict(res.headers))
