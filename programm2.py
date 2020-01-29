import hr1
import employees
#добавили систему продуктивности
import productivity

manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = hr1.PayrollSystem()
payroll_system.calculate_payroll(company_employees)

"""
Программа создает список сотрудников разных типов. 
Список сотрудников отправляется в систему производительности для отслеживания их работы в течение 40 часов.
 Затем тот же список сотрудников отправляется в систему расчета заработной платы.
"""