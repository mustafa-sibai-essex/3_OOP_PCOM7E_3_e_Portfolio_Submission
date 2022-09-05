class Employee:
    def __init__(self, name, email, phone_number, department):
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._department = department

    def __str__(self):
        return """name: {0}
email: {1}
phone number: {2}
department: {3}
""".format(
            self._name, self._email, self._phone_number, self._department
        )
