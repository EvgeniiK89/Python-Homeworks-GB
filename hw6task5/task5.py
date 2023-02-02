"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод
выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение
метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра."""

class Stationary:
    def __init__(self, title= 'tool'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        self.title = 'шариковая ручка'
        print(f'При создании рисунка использовалось: {self.title}')


class Pencil(Stationary):

    def draw(self):
        self.title = 'карандаш'
        print(f'При создании рисунка использовалось: {self.title}')


class Handle(Stationary):

    def draw(self):
        self.title = 'маркер'
        print(f'При создании рисунка использовалось: {self.title}')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
