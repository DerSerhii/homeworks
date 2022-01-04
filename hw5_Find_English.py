""" Урок 5. Практика. Задание 3
    Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле,
    но через функции и map, без единого цикла! """

import re

file_input = 'find_english_text.txt'

with open(file_input, 'r', encoding='utf-8') as file:
    text = str(file.read())


def spotEnglishWords(word):
    eng_word = re.search(r'[A-Za-z]+', word)
    return 1 if bool(eng_word) else 0


result = sum(list(map(spotEnglishWords, text.split())))
print(f"The amount of English words in the '{file_input}' - {result}\n")
