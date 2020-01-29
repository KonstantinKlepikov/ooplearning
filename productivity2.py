# после раздела функционала на то, что относится к производительности и то что относится к системе расчета ЗП

"""
Модуль производительности реализует класс ProductivitySystem, а также связанные с ним роли. 
Классы реализуют интерфейс work(), требуемый системой, но они не получены от Employee.
"""

class ProductivitySystem:
    """
    Класс ProductivitySystem определяет некоторые роли, используя строковый идентификатор, 
    сопоставленный с классом роли, который реализует роль. Он предоставляет метод .get_role(), 
    который при наличии идентификатора роли возвращает объект типа роли. Если роль не найдена, 
    возникает исключение ValueError.

    Он также реализует предыдущую функциональность в методе .track(), где, учитывая список сотрудников, 
    отслеживается производительность этих сотрудников.
    """
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()
        
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')

class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'

class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'

class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'

"""
Каждая из реализованных вами ролей предоставляет функцию .perform_duties(), которая принимает 
количество отработанных часов. Методы возвращают строку, представляющую обязанности.

Классы ролей не зависят друг от друга, но они предоставляют один и тот же интерфейс, поэтому они взаимозаменяемы
"""