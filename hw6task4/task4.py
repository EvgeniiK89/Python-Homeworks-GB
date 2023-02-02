"""4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда); опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля; для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости."""

class Car():

    def __init__(self, speed, color, name, is_police):
        self.max_speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Выбран автомобиль: {name}, цвет {color}')

    def show_speed(self, speed):

        self.speed = speed
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed  > self.speed and not self.is_police:
            print('Превышение скорости!')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это автомобиль городского класса')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это спортивный автомобиль')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Автомобиль для работы')

    def show_speed(self, speed):

        self.speed = speed
        super().show_speed(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Полицейский автомобиль')


my_family_car = TownCar(60, 'красный', 'Nissan Quashkai', False)
my_family_car.go()
my_family_car.show_speed(40)
my_family_car.show_speed(50)
my_family_car.show_speed(60)
my_family_car.turn('направо')
my_family_car.turn('налево')
my_family_car.stop()
print()

my_work_car = WorkCar(60, 'черный', 'Dodge RAM', False)
my_work_car.go()
my_work_car.show_speed(40)
my_work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Ford Mondeo', True)
print()

sport_car = SportCar(60, 'зеленый', 'Toyota Supra', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()