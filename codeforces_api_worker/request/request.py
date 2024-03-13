import requests
import time

from .generator_rand_string import generate_random_string
from .generator_api_sig import generate_api_sig

def request(method_name:str, parameters:dict, key:str = None, secret:str = None):
    url = 'https://codeforces.com/api/'
    parameters['lang'] = 'ru'

    # Формирование подписи для авторизированного запроса
    if all([key, secret]):
        parameters['apiKey'] = key
        parameters['time'] = int(time.time())

        rand = generate_random_string(6)
        api_sig = generate_api_sig(rand, method_name, parameters, secret)
        parameters['apiSig'] = rand + api_sig

    # Формирование URL с параметрами запроса
    url = f'{url}{method_name}?'
    url += '&'.join([f"{key}={value}" for key, value in parameters.items()])

    # Отправка GET запроса
    response = requests.get(url)

    return response


if __name__ == "__main__":
    print("gay sex")