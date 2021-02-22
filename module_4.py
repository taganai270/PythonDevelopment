'''
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат
'''


class Car:

    speed = int
    color = str
    name = str
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''

    def go(self,):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self, direction):
        if direction == 'right':
            return f'{self.name} turn on {direction}'
        elif direction == 'left':
            return f'{self.name} turn on {direction}'
        else:
            return f'invalid direction'

    def show_speed(self):
        return f'Current speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 0 and self.speed <= 60:
            return f'Current speed is {self.speed}'
        elif self.speed >= 60 and self.speed < 180:
            return f'Speed {self.speed} is too high for {self.name}'
        else:
            return 'invalid speed'



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 0 and self.speed <=40:
            return f'Current speed is {self.speed}'
        elif self.speed >= 40 and self.speed < 180:
            return f'Speed {self.speed} is too high for {self.name}'
        else:
            return 'invalid speed'



class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


mazda = TownCar(60, 'white', 'mazda', False)
vaz = SportCar(110, 'red', 'vaz', False)
man = WorkCar(80, 'black', 'man', False)
uaz = PoliceCar(60, 'blue', 'uaz', True)
print(mazda.go(), mazda.show_speed())
print(f'{vaz.go()}, {vaz.turn("right")}, {vaz.show_speed()}')
print(f'{man.go()}, {man.turn("left")}, {man.show_speed()}')








