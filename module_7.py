def fact(n):
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i += 1
        yield f
n = int(input('Узнать Факториал числа: '))
for el in fact(n):
    print(el)
print(f'Факториал числа {n} - {el}')






