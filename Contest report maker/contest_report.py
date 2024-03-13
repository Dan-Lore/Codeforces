import subprocess
import json
import pandas as pd

contest_id = 509421

base_path = 'CODE work/Codeforces/'
contest_standings_json_path = base_path + f'contest.standings_{contest_id}.json'
new_excel_path = base_path + f'contest.report_{contest_id}.xlsx'

# Открываем исходный файл JSON
with open(contest_standings_json_path, 'r') as file:
    data = json.load(file)

# Извлекаем данные из ключа "result"
problems = list(map(lambda key: key['index'], data['result']['problems']))
rows = data['result']['rows']

for row in rows:
    members = map(lambda key: key['handle'], row['party']['members'])
    # for i, member in enumerate(members):
    #     time.sleep(2)
    #     res = requests.get(f'https://codeforces.com/api/user.info?handles={member}')
    #     res = res.json()['result'][0]
    #     last_name = res.get('lastName')
    #     first_name = res.get('firstName')
    #     if first_name or last_name:
    #         member =  last_name + ' ' + first_name 
    #     print(member)
    row['members'] = ', '.join(members)
    row['problem_results'] = list(map(lambda key: '+' if key['points'] else '-', row['problemResults']))

# Создаем DataFrame с нужными колонками
df = pd.DataFrame(rows, columns=['rank', 'members', 'points', 'penalty', 'problem_results'])
df[problems] = pd.DataFrame(df['problem_results'].tolist(), index=df.index)
df = df.drop(columns=['problem_results'])

# Записываем DataFrame в файл Excel
df.to_excel(new_excel_path, index=False)

print('Данные успешно сохранены в новом файле Excel.')