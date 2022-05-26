"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect


FILE_NAME = 'test_file.txt'
with open(FILE_NAME, 'rb') as file:
    words = file.read()
ENCODING = detect(words)['encoding']
print(ENCODING)

with open(FILE_NAME, encoding=ENCODING) as file:
    print(type(file))
    for word in file:
        print(word, end='')
