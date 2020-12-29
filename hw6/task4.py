# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color - color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def show_speed(self):
        return f'скорость {self.name} равна {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super.__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущую скорость автомобиля {self.name} : {self.speed}')

        if self.speed > 40:
            return f'скорость автомобиля {self.name} выше допустимой'
        else:
            return f'скорость автомобиля {self.name} не выше допустимой'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super.__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущую скорость автомобиля {self.name} : {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super.__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущую скорость автомобиля {self.name} : {self.speed}')
        if self.speed > 60:
            return f'скорость автомобиля {self.name} выше допустимой'
        else:
            return f'скорость автомобиля {self.name} не выше допустимой'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super.__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущую скорость автомобиля {self.name} : {self.speed}')

    def police(self):
        if self.is_police:
            return f'{self.name} из департамента полиции'
        else:
            return f'{self.name} не из департамента полиции'


lada = PoliceCar(60, 'Камо', 'Лада', True)
toyota = TownCar(59, 'Красный', 'Камри', False)
ferrari = SportCar(130, 'Желтый', 'Авентадор', False)
cherry = WorkCar(33, 'Белый', 'Безымянный', False)


print(toyota.show_speed())
print(ferrari.show_speed())
print(cherry.show_speed())
print(lada.show_speed())

#не пойму где косяк