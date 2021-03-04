"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Data:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_int(cls, date):
        date_rep = date.replace('-', '')
        day = int(date_rep[:2])
        month = int(date_rep[2:4])
        year = int(date_rep[4:])
        return Data.correct_date(day, month, year)

    @staticmethod
    def correct_date(day, month, year):
        if month < 0 or month > 12:
            return 'wrong month'
        elif day < 0 or day > 31:
            return 'wrong day'
        elif year > 2021 or year < 0:
            return 'wrong year'
        else:
            return '- is a correct date'


d = Data('11-14-2020')
print(d.date, Data.date_int('11-14-2002'))
d1 = Data('11-12-2020')
print(d1.date, Data.date_int('11-12-2020'))
