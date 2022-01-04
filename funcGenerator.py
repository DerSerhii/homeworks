import random as r


def generator(file_output='number.txt'):

    array = [[r.randint(0, 20) for j in range(3)] for i in range(20)]

    with open(file_output, 'x') as file:
        for line in array:
            for num in line:
                print(num, end=' ', file=file)
            print(file=file)

    return file_output
