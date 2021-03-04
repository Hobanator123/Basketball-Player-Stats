class Company:
    all_employees = []
    list_of_positions = ['HourlyEmployee', 'SalariedEmployee', 'Manager', 'Executive']

    def __init__(self):  # In case later want to create multiple companies
        pass

    @classmethod
    def fire(cls, emp_to_fire):
        for emp_info in cls.all_employees:
            if emp_to_fire.fullname() in emp_info:  # If they are an Employee
                cls.all_employees.remove(emp_info)  # Remove from list of Employees
                print('Employee fired')
                return True
        print('Not an employee of company')
        return False

    @classmethod
    def promote(cls, emp_to_raise):
        for emp_info in cls.all_employees:
            if emp_to_raise.fullname() in emp_info:  # If they are an Employee
                if emp_info[1] == 'HourlyEmployee':  # If hourly, raise to salary
                    first, last = emp_to_raise.fullname().split(' ')
                    choose_gross_pay = int(input('Gross Pay: '))
                    choose_pay_periods = int(input('Pay Periods: '))
                    cls.all_employees.remove(emp_info)
                    return SalariedEmployee(first, last, choose_gross_pay, choose_pay_periods)

                elif emp_info[1] == 'SalariedEmployee':  # If salary, raise to manager
                    first, last = emp_to_raise.fullname().split(' ')
                    choose_salary = int(input('Salary: '))
                    cls.all_employees.remove(emp_info)
                    return Manager(first, last, choose_salary)

                elif emp_info[1] == 'Manager':  # If manager, raise to executive
                    first, last = emp_to_raise.fullname().split(' ')
                    choose_base_salary = int(input('Base Salary: '))
                    choose_bonuses = int(input('Bonuses: '))
                    cls.all_employees.remove(emp_info)
                    return Executive(first, last, choose_base_salary, choose_bonuses)

                elif emp_info == 'Executive':  # Executive is highest position in company
                    print(emp_to_raise.fullname() + " can't be promoted further")
                    return True

        print('Not an employee of company')
        return False

    @classmethod
    def hire(cls, first, last, position):
        if position in cls.list_of_positions:
            if position == 'HourlyEmployee':
                choose_hrly_pay = int(input('Hourly pay: '))
                return HourlyEmployee(first, last, choose_hrly_pay)

            elif position == 'SalariedEmployee':
                choose_gross_pay = int(input('Gross Pay: '))
                choose_pay_periods = int(input('Pay Periods: '))
                return SalariedEmployee(first, last, choose_gross_pay, choose_pay_periods)

            elif position == 'Manager':
                choose_salary = int(input('Salary: '))
                return Manager(first, last, choose_salary)

            elif position == 'Executive':
                choose_base_salary = int(input('Base Salary: '))
                choose_bonuses = int(input('Bonuses: '))
                return Executive(first, last, choose_base_salary, choose_bonuses)

        else:
            print('Not a position')
            return False


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = '{}.{}@email.com'.format(first, last)

    def __repr__(self):
        rep = "Employee('{}', '{}')".format(self.first, self.last)
        return rep

    def __str__(self):
        return 'Name: {}\nE-Mail: {}'.format(self.first + self.last, self.email)

    def fullname(self):
        return self.first + ' ' + self.last


# Subclass of Employee
class HourlyEmployee(Employee, Company):
    def __init__(self, first, last, hrly_pay):
        super().__init__(first, last)
        self.hrly_pay = hrly_pay
        self.job_title = 'HourlyEmployee'
        Company.all_employees.append([self.fullname(), self.job_title])  # Adds employee to list of employees


# Subclass of Employee
class SalariedEmployee(Employee, Company):
    def __init__(self, first, last, gross_pay, pay_periods):
        super().__init__(first, last)
        self.gross_pay = gross_pay
        self.pay_periods = pay_periods
        self.emp_salary = gross_pay * pay_periods
        self.job_title = 'SalariedEmployee'
        Company.all_employees.append([self.fullname(), self.job_title])  # Adds employee to list of employees


# Subclass of Employee
class Manager(Employee, Company):
    def __init__(self, first, last, mgr_salary):
        super().__init__(first, last)
        self.mgr_salary = mgr_salary
        self.job_title = 'Manager'
        Company.all_employees.append([self.fullname(), self.job_title])  # Adds employee to list of employees


# Subclass of Employee
class Executive(Employee, Company):
    def __init__(self, first, last, base_salary, bonuses):
        super().__init__(first, last)
        self.base_salary = base_salary
        self.bonuses = bonuses
        self.tot_pay = base_salary + bonuses
        self.job_title = 'Executive'
        Company.all_employees.append([self.fullname(), self.job_title])  # Adds employee to list of employees


# Examples of uses of objects and methods

emp1 = HourlyEmployee('Bob', 'Dylan', 7.35)
emp2 = SalariedEmployee('Charlie', 'Chaplin', 800, 12)
emp3 = Manager('Sarah', 'Mclaughlin', 80000)
emp4 = Executive('Ryan', 'Adams', 100000, 15000)

print(Company.all_employees)
Company.fire(emp1)
print(Company.all_employees)
emp2 = Company.promote(emp2)
print(Company.all_employees)
emp5 = Company.hire('Paul', 'Rudd', 'SalariedEmployee')
print(Company.all_employees)
print(emp5.fullname())
print(emp2.job_title)
print(emp1.email)
