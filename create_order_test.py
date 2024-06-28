# Александра Звагельская, 17-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import requests
import configuration
import data



#Тест на получения заказа по трэку
def test_positive_assert():
    response_create = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body)
    track = response_create.json()["track"]
    response_get = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))
    assert response_get.status_code == 200


