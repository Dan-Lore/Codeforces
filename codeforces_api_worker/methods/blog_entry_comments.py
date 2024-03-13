import json

from codeforces_api_worker.request import request


def get_blog_entry_comments(blogEntryId:int):
    method_name = 'blogEntry.comments'
    parameters = {key: value for key, value in locals().items() if value is not None}
    response = request.request(method_name, parameters)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Сохранение ответа в файл JSON
        data = response.json()
        with open(f'{method_name}_{blogEntryId}.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print('JSON успешно сохранен!')
    else:
        print(f'Произошла ошибка при отправке запроса. Код ошибки: {response.status_code}')