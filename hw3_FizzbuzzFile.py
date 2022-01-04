# -*- coding: utf-8 -*-

import os
from funcFizzBuzz import fizzbuzz
from funcGenerator import generator


def filename(goal, r=False):
    diff = "a different " if r else ""
    return input(f'\033[33mEnter {diff}filename to {goal} (without extension): ') + '.txt'


result = []

file_input = filename('read the data')
if not os.path.exists(file_input):
    print(f"File is missing :(\nRunning the generator to create the file\nData file '{file_input}' created")
    generator(file_input)

with open(file_input) as file:
    data = file.readlines()
    print('\033[0mThe calculation results:')
    for line in data:
        fizz, buzz, razz = map(int, line.split())
        row = fizzbuzz(fizz, buzz, razz)
        result.append(f'{data.index(line) + 1} row:\t\t{fizz}\t{buzz}\t{razz}\t\t==> fizzbuzz ==>\t{row}')
        print(result[data.index(line)])

file_output = filename('save the results')
while os.path.exists(file_output):
    file_output = filename('save the results', True)

with open(file_output, 'x') as file:
    for line in result:
        print(result[result.index(line)], file=file)
    print(f"Calculation results are written to '{file_output}'")
