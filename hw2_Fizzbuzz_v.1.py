# -*- coding: utf-8 -*-

# entering three numbers into the console and assign them to variables
fizz, buzz, razz = map(int, input("Введите три числа через пробел: ").split())

# final output
for number in range(1, razz + 1):
    if number % fizz == number % buzz == 0:
        print("FB", end='\t')
    elif number % fizz == 0:
        print("F", end='\t')
    elif number % buzz == 0:
        print("B", end='\t')
    else:
        print(number, end='\t')
print()  # reset (end='\t')


