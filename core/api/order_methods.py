import requests
import allure
from core.utils.urls import Urls

class OrderMethods:
    @staticmethod
    def make_order(body, headers=None):
        with allure.step('Создание заказа'):
            return requests.post(url=Urls.MAKE_ORDER_ENDPOINT, headers=headers, json=body)
