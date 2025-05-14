import requests
from urls import Urls
import random
import string


# Функция для генерации случайной строки (для email, пароля, имени)
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Функция для регистрации нового пользователя
def register_new_user_and_return_login_password():
    email = f"test_{generate_random_string(8)}@yandex.ru"
    password = generate_random_string(10)
    name = f"User_{generate_random_string(6)}"

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Urls.REGISTER_API, json=payload)  # Используем REGISTER_API URL для регистрации
    if response.status_code == 200:
        return {
            "status_code": response.status_code,
            "email": email,
            "password": password,
            "name": name,
            "response_data": response.json()
        }
    else:
        raise Exception(f"Ошибка регистрации: {response.status_code} - {response.text}")

def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(Urls.LOGIN_API, json=payload)  # Используем LOGIN_API URL для авторизации
    if response.status_code == 200:
        return response.json()['accessToken']  # Возвращаем токен
    else:
        raise Exception(f"Ошибка авторизации: {response.status_code} - {response.text}")

def delete_user(email, password):
    # Получаем токен
    token = login_user(email, password)
    headers = {"Authorization": token}

    response = requests.delete(Urls.DELETE_USER, headers=headers)
    if response.status_code == 202:
        return response.status_code
    else:
        raise Exception(f"Ошибка удаления пользователя: {response.status_code} - {response.text}")