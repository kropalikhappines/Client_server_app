"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com 
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for arg in ARGS:
    YA_PING = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        # print(line)
        line_decode = chardet.detect(line)
        line = line.decode(line_decode['encoding'])
        print(f'{line} тип "{type(line)}"')
        # line_encode = line.encode('ascii')
        # line = line.decode(result['encoding']).encode('utf-8')
        # print(line.decode('utf-8'))