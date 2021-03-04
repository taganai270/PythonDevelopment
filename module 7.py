"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = complex(a, b)

    def __add__(self, other):
        print(f'The sum of z1 and z2 is')
        return f'z = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'The product of z1 and z2 is')
        return f'z = {self.a * other.a + self.b * other.a} + {self.a * other.b + self.b * other.b}'


z_1 = ComplexNumber(7, 6)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
