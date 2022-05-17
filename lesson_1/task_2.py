'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode
и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

class_ = b'class'
function_ = b'function'
method_ = b'method'
words = [class_, function_, method_]

for word in words:
    print(f'Слово {word}, тип {type(word)}, длинна {len(word)}')
