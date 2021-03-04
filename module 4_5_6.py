"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.

"""


class LocalError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:

    def __init__(self, name, quantity, cost, weight):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.weight = weight
        self.stock_availability = bool
        self.store_full = []
        self.equipment_store = []
        self.equipment_unit = {'Модель': self.name, 'Цена за ед': self.cost,
                               'Количество': self.quantity, 'Вес': self.weight}

    def getting(self):

        try:
            unit = input('Введите наименование ')
            unit_c = float(input('Введите цену за ед '))
            unit_q = int(input('Введите количество '))
            unit_w = float(input('Введите вес в кг '))
            unique = {'Модель': unit, 'Цена за ед': unit_c,
                      'Количество': unit_q, 'Вес': unit_w}
            self.equipment_unit.update(unique)
            self.equipment_store.append(self.equipment_unit)
            print(f'Текущий список -\n {self.equipment_store}')
            if unit_c <= 0 or unit_q < 0 or unit_w <= 0:
                raise LocalError('Ввод не корректен, отрицательное значение!')
        except (ValueError, LocalError) as err:
            return err
        else:
            return 'Ошибка ввода данных'

        q = input('Для выхода - Q, продолжение - Enter')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.equipment_store)
            print(f'Весь склад -\n {self.store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.getting(self)


class Printer(OfficeEquipment):
    def __init__(self, max_print_size, printing_method, name, quantity, cost, weight):
        super().__init__(name, quantity, cost, weight)
        self.max_print_size = max_print_size
        self.printing_method = printing_method


class Scanner(OfficeEquipment):
    def __init__(self, scanner_type, scan_size, name, quantity, cost, weight):
        super().__init__(name, quantity, cost, weight)
        self.scanner_type = scanner_type
        self.scan_size = scan_size


class Photocopier(OfficeEquipment):
    def __init__(self, copier_type, print_speed, name, quantity, cost, weight):
        super().__init__(name, quantity, cost, weight)
        self.copier_type = copier_type
        self.print_speed = print_speed
