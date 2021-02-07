
def str_num():
    sum_total = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел, или "q" - для выхода: ').split()

        n = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                break
            else:
                n = n + int(number[i])
        sum_total = sum_total + n
        print(f'Сумма равна  {sum_total}')
    print(f'Общая сумма равна  {sum_total}')

str_num()
