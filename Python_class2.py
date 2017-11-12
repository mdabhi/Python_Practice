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
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# Assigning employee names and salary to emp_str
emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Jane-Doe-90000'
emp_str4 = 'Prakash-Dabhi-100000'

# Creating the new objects from given strings separated by '-'
new_emp1 = Employee.from_string(emp_str1)
new_emp2 = Employee.from_string(emp_str2)
new_emp3 = Employee.from_string(emp_str3)
new_emp4 = Employee.from_string(emp_str4)


print(new_emp1.__dict__)
print(new_emp2.__dict__)
print(new_emp3.__dict__)
print(new_emp4.__dict__)
