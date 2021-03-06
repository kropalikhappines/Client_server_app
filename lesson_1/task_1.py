"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить
в строковом формате и проверить тип и содержание соответствующих
переменных. Затем с помощью онлайн-конвертера преобразовать
строковые представление в формат Unicode и также проверить тип и содержимое переменных.
"""


words = ['разработка', 'сокет', 'декоратор']
for word in words:
    print(f'Содержимое "{word}", тип {type(word)}, Unicode "{word.encode("unicode_escape")}"')
    word_unicode = word.encode('unicode_escape')
    print(f'Содержимое "{word_unicode}", тип {type(word_unicode)}\n')
