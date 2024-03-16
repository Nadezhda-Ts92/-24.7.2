import json
import requests

# GET запрос
get_response = requests.get("https://petstore.swagger.io/v2/swagger.json", headers={'accept': 'application/json'})
print("GET запрос:")
print("Статус код:", get_response.status_code)
print("Текст ответа:", get_response.text)
print("JSON ответа:", get_response.json())
print("Тип JSON ответа:", type(get_response.json()))
print()

# POST запрос (Пример данных для питомца)
pet_data = {
    "id": 9999,
    "category": {
        "id": 1,
        "name": "dog"
    },
    "name": "Rex",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
post_response = requests.post("https://petstore.swagger.io/v2/swagger.json", json=pet_data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print("POST запрос:")
print("Статус код:", post_response.status_code)
print("Текст ответа:", post_response.text)
print()

# PUT запрос (Пример обновленных данных для питомца)
pet_update_data = {
    "id": 9999,
    "name": "Rex Updated",
    "status": "sold"
}
put_response = requests.put("https://petstore.swagger.io/v2/swagger.json", json=pet_update_data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print("PUT запрос:")
print("Статус код:", put_response.status_code)
print("Текст ответа:", put_response.text)
print()

# DELETE запрос (ID питомца для удаления)
pet_id_to_delete = 9999
delete_response = requests.delete(f"https://petstore.swagger.io/v2/swagger.json/{pet_id_to_delete}", headers={'accept': 'application/json'})
print("DELETE запрос:")
print("Статус код:", delete_response.status_code)
print("Текст ответа:", delete_response.text)
