import json

from codeforces_api_worker.request import request


def get_constest_hacks(contestId:int, asManager:bool=None):
    method_name = 'contest.hacks'

    #params = filter(lambda key, value: value is not None, locals().items())
    parameters = {key: value for key, value in locals().items() if value is not None}

    if parameters['asManager']:
        with open('data.json', 'r') as f:
            data = json.load(f)
            key = data['key']
            secret = data['secret']
        response = request.request(method_name, parameters, key, secret)
    else:
        response = request.request(method_name, parameters)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Сохранение ответа в файл JSON
        data = response.json()
        with open(f'{method_name}_{contestId}.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print('JSON успешно сохранен!')
    else:
        print(f'Произошла ошибка при отправке запроса. \
              Код ошибки: {response.status_code}')