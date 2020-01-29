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