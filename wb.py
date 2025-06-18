import requests
from typing import Optional

def get_wb_info(article: str) -> Optional[dict]:
    try:
        url = 'https://card.wb.ru/cards/v2/detail' # Указал ссылку на API
        parametrs = { # Это словарь с параметрами запроса
            'appType': 1,
            'curr': 'rub',
            'dest': -445284,
            'hide_dtype': 13,
            'spp': 30,
            'ab_testing': 'false',
            'lang': 'ru',
            'nm': article
        }

        response = requests.get(url, params=parametrs) # Отправляем запрос get с параметрами 
        data = response.json() # Здесь преобразовал ответ в json формат, чтобы получить словарь
        products = data['data']['products'] # Получаем список товаров

        if len(products) == 0:# Если товаров нет, возвращаем None
            return None
        
        product = products[0]# Берем товар из списка, он там единственный, потому что один артикул
        name = product['name']# Получем наименование товара

        sizes = product['sizes']# Получаем список 'sizes', так как в нем хранится 'price'
        price_cop = sizes[0]['price']['total'] # Получаем итоговую цену
        price_val = sizes[0]['price']['product'] # А это цена со скидкой
        # Значения указаны в копейках, поэтому преобразовал в рубли
        price = price_cop // 100
        price1 = price_val // 100

        return {'name': name, 'price': price, 'priceval':price1} # Возвращаем словарь
    except:
        return 'Ничего не найдено'

info = get_wb_info('238438401')
print(info)
