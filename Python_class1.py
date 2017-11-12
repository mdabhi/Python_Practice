#!/bin/python3.6

"""
This code is for learning and practicing the OOPs concepts...

"""


class Employee:
    raise_amount = 1.04
    num_of_emp  = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com' 
        self.pay = pay
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

emp_1=Employee('Minita', 'Dabhi', 50000)
emp_2=Employee('Test', 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print('{} {}'.format(emp_1.first, emp_1.last))
# print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.__dict__)
print(Employee.num_of_emp)
