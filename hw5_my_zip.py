number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(f"built-in function ZIP: \t{list(zip(number, char))}")
print(f"my function ZIP: \t\t{list(map(lambda x, y: (x, y), number, char))}")