from abc import ABC, abstractmethod

class IDepartment(ABC):

    @abstractmethod
    def __init__(self, employees):
        pass

    @abstractmethod
    def print_data(self):
        pass

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_data(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_data(self):
        print(f"Development Department: {self.employees}")

class Company(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        self.employees += department.employees

    def print_data(self):
        print(f"Company: {self.employees}")
        print(f"Base Employees: {self.base_employees}")
        for department in self.departments:
            department.print_data()


accounting = Accounting(10)
development = Development(25)

company = Company(5)
company.add_department(accounting)
company.add_department(development)

company.print_data()