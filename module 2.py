"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero:

    def __init__(self, divisible, divider):
        self.divider = divider
        self.divisible = divisible

    def zero_check(self):
        try:
            return self.divisible / self.divider
        except:
            return 'cannot be divided by zero'


d = DivisionByZero(120, 10)
print(d.zero_check())
d1 = DivisionByZero(120, 0)
print(d1.zero_check())
