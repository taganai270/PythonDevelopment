def quotient():
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        return a / b
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
    finally:
        print('Выход из фукции')











