from ast import increment_lineno
from sys import settrace


class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self,val):
        self.increment = val/self.salary
    

e = Employee()
print(e.increment)
e.salaryAfterIncrement = 20000
print(e.increment)