class Holiday:
    def __init__(self, employee, start_date, duration):
        self._employee = employee
        self._start_date = start_date
        self.duration = duration

    def __str__(self):
        return """employee: {0}
starting date: {1}
duration: {2}
---------------
""".format(
            self._employee, self._start_date, self.duration
        )
