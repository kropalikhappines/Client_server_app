"""
3. Определить, какие из слов «attribute», «класс»,
«функция», «type» невозможно записать в байтовом типе.
"""
words = ['attribute', 'класс', 'функция', 'type']


for word in words:
    try:
        print('Преобразованно в байт тип', eval(f'b"{word}"'))
    except SyntaxError:
        print('Нельзя преобразовать', word)
