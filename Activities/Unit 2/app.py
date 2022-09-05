# Optional extension activities
# Write a Python program to achieve basic employee-related functionality which includes
# retaining employee details and allowing an employee to book a day of annual leave.
# Extend the Python program you have now created to use protected and unprotected variables.
# Remember to record your findings in your e-portfolio.
# ---------------------------------------------------------------------------------------------
# In this program there are three classes. The employee class which contains all of the employee data like
# name, email, date of birth and department. The class implements the __str__ function which returns a string
# of all of its data. There is also the holiday class which contains data about employee holidays like employee,
# holiday start date and duration. Finally there is the annualLeaveTable which has an array of holidays and
# a function to add a new employee holiday.

from employee import *
from annualLeaveTable import *

employees = [
    Employee("John", "John@yahoo.com", 55776688, "Marketing"),
    Employee("David", "David@yahoo.com", 89838412, "Dev Team"),
    Employee("Will", "Will@yahoo.com", 746573922, "Admin"),
    Employee("Tylar", "Tylar@yahoo.com", 746573922, "HR"),
]

for employee in employees:
    print(employee)

table = AnnualLeaveTable(2022)
table.AddEmployee(employees[0], "05/08/2022", "2w")
table.AddEmployee(employees[2], "09/11/2022", "3w")

print(table)
