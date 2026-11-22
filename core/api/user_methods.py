import requests
import allure
from core.utils.urls import Urls

class UserMethods:
    @staticmethod
    def create_user(body):
        with allure.step('Создание пользователя'):
            return requests.post(url=Urls.REGISTER_ENDPOINT, json=body)
            
    @staticmethod
    def delete_user(access_token):
        with allure.step('Удаление пользователя'):
            return requests.delete(url=Urls.DELETE_USER_ENDPOINT, headers={'Authorization': access_token})

    @staticmethod
    def login_user(email, password):
        body = {
            "email": email,
            "password": password
        }
        with allure.step('Авторизация пользователя'):
            return requests.post(url=Urls.LOGIN_ENDPOINT, json=body)
