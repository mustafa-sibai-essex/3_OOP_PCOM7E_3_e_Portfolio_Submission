from holiday import *


class AnnualLeaveTable:
    def __init__(self, year):
        self._year = year
        self._leavesTable: Holiday = []

    def __str__(self):
        table = ""
        table += """Annual leave table for the year {0}
-------------------------------------
""".format(
            self._year
        )

        for leaveEntery in self._leavesTable:
            table += leaveEntery.__str__()

        return table

    def AddEmployee(self, employee, start_date, duration):
        self._leavesTable.append(Holiday(employee, start_date, duration))
