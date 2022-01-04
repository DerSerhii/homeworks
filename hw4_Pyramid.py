
medNum = 17

i = 1
while i <= medNum:
    huph = '-' * (medNum - i)
    sharp = '#' * (2 * i - 1)
    print(huph + sharp + huph)
    i += 1


