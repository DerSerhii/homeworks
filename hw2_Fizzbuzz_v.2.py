# -*- coding: utf-8 -*-

from funcFizzBuzz import fizzbuzz

fizz, buzz, razz = map(int, input("Введите три числа через пробел: ").split())

print(fizzbuzz(fizz, buzz, razz))
