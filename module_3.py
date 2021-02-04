number = int(input('Введите порядковый номер месяца, от 1 до 12: '))
while number < 1 or number > 12:
    print('Ввод не корректен, попробуйте ещё')
    number = int(input('Введите порядковый номер месяца, от 1 до 12: '))

monhts = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
          7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

if 1 < number <= 2 or number == 12:
    print(f'{number} - это зимний месяц  {monhts.get(number)}')
elif 3 < number <= 5:
    print(f'{number} - это весенний месяц  {monhts.get(number)}')
elif 6 < number <= 8:
    print(f'{number} - это летний месяц  {monhts.get(number)}')
else:
    print(f'{number} - это осенний месяц  {monhts.get(number)}')



