import hr2
import employees1
#добавили систему продуктивности
import productivity1
import contacts

manager = employees1.Manager(1, 'Mary Poppins', 3000)
manager.address = contacts.Address(
    '121 Admin Rd', 
    'Concord', 
    'NH', 
    '03301'
)
secretary = employees1.Secretary(2, 'John Smith', 1500)
secretary.address = contacts.Address(
    '67 Paperwork Ave.', 
    'Manchester', 
    'NH', 
    '03101'
)
sales_guy = employees1.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees1.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees1.TemporarySecretary(5, 'Robin Williams', 40, 9)
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity1.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = hr2.PayrollSystem()
payroll_system.calculate_payroll(company_employees)