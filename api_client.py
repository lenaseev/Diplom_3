import requests
from urls import Urls
from helpers import generate_random_string
import allure


@allure.step("Функция для регистрации нового пользователя")
def register_new_user_and_return_login_password():
    email = f"test_{generate_random_string(8)}@yandex.ru"
    password = generate_random_string(10)
    name = f"User_{generate_random_string(6)}"

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Urls.REGISTER_API, json=payload)
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

@allure.step("Логин пользователя в систему")
def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(Urls.LOGIN_API, json=payload)
    if response.status_code == 200:
        return response.json()['accessToken']  # Возвращаем токен
    else:
        raise Exception(f"Ошибка авторизации: {response.status_code} - {response.text}")

@allure.step("Удаление пользователя")
def delete_user(email, password):
    # Получаем токен
    token = login_user(email, password)
    headers = {"Authorization": token}

    response = requests.delete(Urls.DELETE_USER, headers=headers)
    if response.status_code == 202:
        return response.status_code
    else:
        raise Exception(f"Ошибка удаления пользователя: {response.status_code} - {response.text}")