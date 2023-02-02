"""3. Реализовать базовый класс Worker (работник). определить атрибуты: name,
surname, position (должность), income (доход); последний атрибут должен быть
защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}; создать класс Position (должность)
на базе класса Worker; в классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров."""

class Worker:

    def __init__(self, name, surname, position, wage=70, bonus=50):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': wage, 'Премия': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['Оклад'] + self._income['Премия']


empl_obj = Position('Иван', 'Петров', 'рабочий', 80, 40)
print(f'Анкета работника/цы: {empl_obj.name}, {empl_obj.surname}, '
      f'{empl_obj.position}, {empl_obj._income}')
print(f'Общий доход работника/цы - {empl_obj.get_full_name()} составляет: '
      f'{empl_obj.get_total_income()}')
