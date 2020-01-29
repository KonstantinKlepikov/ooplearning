from productivity2 import ProductivitySystem
from hr3 import PayrollSystem
from contacts1 import AddressBook

class EmployeeDatabase:

    """
    EmployeeDatabase отслеживает всех сотрудников компании. Для каждого сотрудника 
    он отслеживает id, name и role. У него есть экземпляр ProductivitySystem, PayrollSystem и AddressBook. 
    Эти экземпляры используются для создания сотрудников.

    Он содержит свойство .employees, которое возвращает список сотрудников. Объекты Employee создаются 
    во внутреннем методе ._create_employee(). Обратите внимание, что у нас нет разных типов классов Employee. 
    Нам просто нужно реализовать один класс Employee
    """
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

class Employee:
    """Класс Employee инициализируется атрибутами id, name и address. Он также требует роли 
    производительности для работника role и политики оплаты труда payroll.

    Класс предоставляет метод .work(), который принимает отработанные часы. Этот метод сначала извлекает 
    обязанности duties из роли role. Другими словами, он делегирует объекту role выполнения своих обязанностей.

    Таким же образом он делегирует объекту payroll отслеживания рабочего времени hours. Заработная плата payroll, 
    как вы видели, использует эти часы для расчета заработной платы, если это необходимо
    """

    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
