import hr

""" В итоге 
Производные классы реализуют интерфейс IPayrollCalculator, который требуется PayrollSystem. 
Реализация PayrollSystem.calculate_payroll() требует, чтобы передаваемые объекты employee 
содержали реализацию id, name и calculate_payroll()

Программа создает три объекта employee, по одному для каждого из производных классов. 
Затем она создает систему начисления заработной платы и передает список сотрудников в метод .calculate_payroll(), 
который рассчитывает начисление заработной платы для каждого сотрудника и печатает результаты.

Базовый класс Employee не определяет метод .calculate_payroll(). Это означает, что если создать простой объект Employee 
и передать его в PayrollSystem, будет ошибка.
"""
salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])