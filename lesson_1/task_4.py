"""
4. Преобразовать слова «разработка», «администрирование»,
«protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    word_encode = str.encode(word, encoding='utf-8')
    print(type(word_encode))
    word_decode = bytes.decode(word_encode, encoding='utf-8')
    print(type(word_decode))

