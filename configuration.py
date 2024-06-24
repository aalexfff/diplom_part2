URL_SERVICE = 'https://580422bb-7d0c-4fd1-8144-4c792f8d1bfd.serverhub.praktikum-services.ru'
CREATE_ORDER ="/api/v1/orders" #создание заказа
GET_ORDER ="/api/v1/orders/?t=" #получение заказа по его номеру

#Тело для создания заказа
order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
