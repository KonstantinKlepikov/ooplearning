# после раздела функционала на то, что относится к производительности и то что относится к системе расчета ЗП

"""
Модуль hr реализует систему PayrollSystem, которая рассчитывает заработную плату для сотрудников. 
Он также реализует классы политики для расчета заработной платы. Как видите, классы политики 
больше не являются производными от Employee
"""

class PayrollSystem:
    """
    Здесь мы проверяем, есть ли у объекта employee адрес, и если он есть, печатаем его
    """
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

class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission