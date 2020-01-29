# после раздела функционала на то, что относится к производительности и то что относится к системе расчета ЗП

"""
Модуль производительности реализует класс ProductivitySystem, а также связанные с ним роли. 
Классы реализуют интерфейс work(), требуемый системой, но они не получены от Employee.
"""

class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')

class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing office paperwork.'

class SalesRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone.'

class FactoryRole:
    def work(self, hours):
        return f'manufactures gadgets for {hours} hours.'