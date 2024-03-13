import json
from pathlib import Path


dir_path = Path(__file__).parent.parent.resolve()

def save_response(response, json_file_name:str):
    json_file_path = dir_path.joinpath(json_file_name + '.json')

    # Проверка статуса ответа
    if response.status_code == 200:
        # Сохранение ответа в файл JSON
        data = response.json()
        with open(json_file_path.as_posix(), 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print('JSON успешно сохранен!')
    else:
        print(f'Произошла ошибка при отправке запроса. \
              Код ошибки: {response.status_code}')