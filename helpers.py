import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# def register_new_user_and_return_login_password():
#     email = f"test_{generate_random_string(8)}@example.com"
#     password = generate_random_string(10)
#     name = f"User_{generate_random_string(6)}"
#
#     payload = {
#         "email": email,
#         "password": password,
#         "name": name
#     }
#
#     response = requests.post(Urls.REGISTER_API, json=payload)
#     if response.status_code == 200:
#         return {
#             "email": email,
#             "password": password,
#             "name": name,
#             "response_data": response.json()
#         }
#     raise Exception(f"Ошибка регистрации: {response.status_code} - {response.text}")
#
#
# def delete_user(email, password):
#     # Логин для получения токена
#     login_response = requests.post(
#         Urls.LOGIN_API,
#         json={"email": email, "password": password}
#     )
#     token = login_response.json().get('accessToken')
#
#     # Удаление пользователя
#     response = requests.delete(
#         Urls.DELETE_USER,
#         headers={"Authorization": token}
#     )
#     if response.status_code != 202:
#         raise Exception(f"Ошибка удаления пользователя: {response.status_code}")