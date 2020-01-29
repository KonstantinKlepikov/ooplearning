class PayrollSystem:
    """
    PayrollSystem реализует метод .calculate_payroll(), который принимает коллекцию 
    сотрудников и печатает их идентификатор, имя и сумму чека, используя метод .calculate_payroll(), 
    представленный для каждого объекта сотрудника.
    """
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee:
    """
    Employee является базовым классом для всех типов сотрудников. Он объявлен с id и name.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    """
    Здесь мы создали производный класс SalaryEmployee, который наследует Employee. 
    Класс инициализируется с помощью id и name, требуемыми базовым классом, и для этого мы 
    используете super() для инициализации членов базового класса. SalaryEmployee также требует 
    параметр инициализации weekly_salary, который представляет сумму, которую сотрудник 
    зарабатывает за неделю.
    """
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    """
    Класс HourlyEmployee инициализируется с помощью id и name, переменных базового класса, 
    плюс hours_worked и hour_rate, необходимые для расчета заработной платы. 
    Метод .calculate_payroll() реализован путем возврата отработанных часов, 
    умноженных на часовую ставку.
    """
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    """
    Получаем CommissionEmployee от SalaryEmployee, потому что оба класса имеют weekly_salary. 
    В то же время, CommissionEmployee инициализируется значением commission, 
    основанным на продажах для сотрудника.

    Поскольку CommissionEmployee является производным от SalaryEmployee, у нас есть доступ 
    к свойству weekly_salary напрямую, и мы могли бы реализовать .calculate_payroll(), используя значение этого свойства.

    Проблема с прямым доступом к свойству заключается в том, что если изменяется реализация 
    SalaryEmployee.calculate_payroll(), нам также придется изменить реализацию CommissionEmployee.calculate_payroll(). 
    Лучше полагаться на уже реализованный метод в базовом классе и расширять функциональность по мере необходимости.
    """
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

