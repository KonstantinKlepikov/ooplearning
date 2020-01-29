"""
Хотя мы можем создать экземпляр объекта Employee, этот объект не может быть использован системой PayrollSystem. 
Потому что он не имеет .calculate_payroll() для Employee. Чтобы соответствовать требованиям PayrollSystem, 
нам нужно преобразовать класс Employee, который в настоящее время является простым классом, в абстрактный класс. 
Таким образом, ни один сотрудник никогда не будет просто Employee, 
а он будет обязательно содержать реализацию .calculate_payroll().
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Мы наследуем Employee от ABC, делая его абстрактным базовым классом. 
    Затем мы декорируем метод .calculate_payroll() с помощью декоратора @abstractmethod
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
    @abstractmethod
    def calculate_payroll(self):
        pass

"""
Результат показывает, что класс не может быть создан, 
поскольку он содержит абстрактный метод calculate_payroll(). 
Производные классы должны переопределять метод, чтобы разрешить создание объектов их типа.
"""
class DisgruntledEmployee:
    """
    Класс DisgruntledEmployee не является производным от Employee, но предоставляет 
    тот же интерфейс, который требуется PayrollSystem. PayrollSystem.calculate_payroll() 
    требует список объектов, которые реализуют следующий интерфейс:

    - Свойство id или атрибут, который возвращает идентификатор сотрудника
    - Свойство name или атрибут, представляющий имя сотрудника
    - Метод .calculate_payroll(), который не принимает никаких параметров и возвращает 
    сумму заработной платы для обработки
    Все эти требования выполняются классом DisgruntledEmployee, поэтому PayrollSystem все 
    еще может рассчитать свою заработную плату.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def calculate_payroll(self):
        return 1000000