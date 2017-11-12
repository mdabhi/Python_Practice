#!/bin/python3.6

"""
This code is for learning and practicing the OOPs concepts...

"""

import datetime


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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1=Employee('Minita', 'Dabhi', 50000)
emp_2=Employee('Test', 'User', 60000)

# Checks if the given date is working day or not and returns True or False accordingly
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

