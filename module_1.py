file_1 = open('text_1.txt', 'w')
f_str = input('Введите данные: ')
while True:
    print(f'{f_str}', file=file_1)
    f_str = input('Введите данные: ')
    if f_str == '':
        break
file_1.close()
