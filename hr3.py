# после раздела функционала на то, что относится к производительности и то что относится к системе расчета ЗП

"""
Модуль hr реализует систему PayrollSystem, которая рассчитывает заработную плату для сотрудников. 
Он также реализует классы политики для расчета заработной платы. Как видите, классы политики 
больше не являются производными от Employee
"""

class PayrollSystem:
    """
    Система PayrollSystem ведет внутреннюю базу данных политик расчета заработной платы для каждого сотрудника. 
    Она предоставляет функцию .get_policy(), которая, учитывая идентификатор сотрудника, возвращает свою политику 
    расчета заработной платы. Если указанный идентификатор не существует в системе, метод вызывает исключение ValueError.

    Реализация .calculate_payroll() работает так же, как и раньше. Он берет список сотрудников, рассчитывает 
    фонд заработной платы и печатает результаты.
    """
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')

class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0
    def track_work(self, hours):
        self.hours_worked += hours

class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

"""
Сначала реализуется класс PayrollPolicy, который служит базовым классом для всех 
политик расчета заработной платы. Этот класс отслеживает часы работы hours_worked, 
которые являются общими для всех политик расчета заработной платы.

Другие классы политик являются производными от PayrollPolicy. Мы используем наследование здесь, 
потому что мы хотим использовать реализацию PayrollPolicy. Кроме того, SalaryPolicy, HourlyPolicy и 
CommissionPolicy являются PayrollPolicy.

SalaryPolicy инициализируется значением weekly_salary, которое затем используется в .calculate_payroll(). 
HourlyPolicy инициализируется с помощью hour_rate и реализует .calculate_payroll(), используя базовый 
класс hours_worked.

Класс CommissionPolicy является производным от SalaryPolicy, потому что он хочет наследовать свою реализацию. 
Он инициализируется с параметрами weekly_salary, но для него также требуется параметр commission_per_sale.

commission_per_sale используется для вычисления .commission, которое реализовано как свойство, поэтому 
она вычисляется по запросу. В этом примере мы предполагаем, что продажа происходит каждые 5 часов работы, 
а .commission – это количество продаж, умноженное на значение commission_per_sale.

CommissionPolicy реализует метод .calculate_payroll(), сначала используя реализацию в SalaryPolicy, а затем 
добавляя рассчитанную комиссию
"""