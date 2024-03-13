import json
import requests
import time

from .generator_rand_string import generate_random_string
from .generator_api_sig import generate_api_sig

def request(method_name:str, parameters:dict):
    url = 'https://codeforces.com/api/'
    parameters['lang'] = 'ru'

    #Какой метод лучше?
    #parameters = filter(lambda key, value: value is not None, locals().items())
    parameters = {key: value for key, value in parameters.items() if value is not None}

    if 'asManager' in parameters and parameters['asManager']:
        with open('data.json', 'r') as f:
            data = json.load(f)
            key = data['key']
            secret = data['secret']
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