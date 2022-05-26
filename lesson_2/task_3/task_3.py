"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
"""

import yaml


file_result = 'file.yaml'
DICT = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_ptice': {'computer': '200в‚¬-1000в‚¬',
                        'keyboard': '5в‚¬-50в‚¬',
                        'mouse': '4в‚¬-7в‚¬',
                        'printer': '100в‚¬-300в‚¬'},
        'items_quantity': 4}

with open(file_result, 'w') as file:
    yaml.dump(DICT, file, default_flow_style=False, allow_unicode=True)
