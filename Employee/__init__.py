"""
program:  Emloyee   Module 11 topic 4
author:  Lisa Kilmer
last modified:  Julu 5, 2020
this is a class Employee as the base class and Salaried Employee and Hourly Employee as derived classes. The first
name and last name come from the Employee class the the rest come from either Salaried Employee or Hourly Employee
 if the employee is salaried or Hourly. It uses def display to print the output and each have a method give_raise to
 increase salary ( they don't work, it wants 2 arguments in the drive but self isn't it, displays correctly till I try
 to raise the salary)   deletes the file to clean up.
"""


class Employee:  #base class

    # Constructor
     def __init__(self, lname, fname):
         self._last_name = lname
         self._first_name = fname

     def set_last_name(self, lname):
         self._last_name = lname

     def set_first_name(self, fname):
         self._first_name = fname

     def __str__(self):
        return self._last_name + self._first_name

     def display(self):
        return self._last_name + " " + self._first_name


class SalariedEmployee(Employee):  #derived class
     def __init__(self, fname, lname, salary, start_date):
        super().__init__(lname, fname)
        self.start_date = start_date
        self.salary = salary

     def set_start_date(self, start_date):
         self.start_date = start_date

     def set_salary(self, salary):
         self.salary = salary

     def give_raise(self, new_salary):
         self.salary = new_salary
         return new_salary

     def display(self):
         return self._last_name + ' ' + self._first_name + ' ' + 'Salary: ' + self.salary + ' ' + self.start_date


class HourlyEmployee(Employee):  #derived class
    def __init__(self, fname, lname, hourly_pay, start_date):
        super().__init__(lname, fname)
        self.hourly_pay = hourly_pay
        self.start_date = start_date

    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay

    def set_start_date(self, start_date):
        self.start_date = start_date

    def give_raise(self, new_hourly_pay):
        self.hourly_pay = new_hourly_pay
        return new_hourly_pay

    def display(self):
        return self._last_name + ' ' + self._first_name + ' ' + 'Hourly pay: ' + self.hourly_pay + ' ' + self.start_date


# Driver
JoeSalariedEmployee = SalariedEmployee('Kilmer', 'Lisa', '$40,000', '7/3/2020')
print(JoeSalariedEmployee.display())
new_salary = SalariedEmployee.give_raise(self, '$45,000')
print(JoeSalariedEmployee.display())
del JoeSalariedEmployee

SamHourlyEmployee = HourlyEmployee('Olson', 'Sara', '$10.00', '7/3/2020')
print(SamHourlyEmployee.display())
hourly_new_salary = HourlyEmployee.give_raise(self, '$12.00 an hour')
print(SamHourlyEmployee.display())
del SamHourlyEmployee
