# Александра Звагельская, 17-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import requests
import configuration

#Функция для создания заказа, возвращает номер заказа
def order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json = configuration.order_body)
    return response.json()["track"]

#Тест на получения заказа по трэку
def test_positive_assert():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "order()")
    assert response.status_code == 200
