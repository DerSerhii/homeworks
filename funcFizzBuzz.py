
def fizzbuzz(fizz, buzz, razz):
    """ function of counting by fizzbuzz method )))"""

    result = ''

    for number in range(1, razz + 1):
        try:
            if number % fizz == number % buzz == 0:
                result += 'FB\t'
            elif number % fizz == 0:
                result += 'F\t'
            elif number % buzz == 0:
                result += 'B\t'
            else:
                result += (str(number) + '\t')
        except ZeroDivisionError:
            return 'Zero is not allowed'
    return result
