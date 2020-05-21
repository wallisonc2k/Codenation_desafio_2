from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
        
    @abstractmethod
    def calc_bonus(self):
        pass
    
    def get_hours(self):
        pass

    def get_departament(self):
        return self._departament.name

    def set_departament(self, name):
        self._departament.name = name

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return self.hours


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, valor):
        self._sales += valor

    def calc_bonus(self):
        return self._sales * 0.15
