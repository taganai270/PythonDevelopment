st = input('Введите слова через пробел: ').split()
n = 1
for world in st:
    print(n, world[:10])
    n +=1

