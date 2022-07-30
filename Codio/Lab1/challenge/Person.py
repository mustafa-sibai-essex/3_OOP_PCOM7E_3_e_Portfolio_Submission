class Person:
    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    def bmi_range_checker(self):
        bmi = self.calc_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi >= 18.5 and bmi < 25.0:
            return "Healthy Weight"
        elif bmi >= 25.0 and bmi < 30.0:
            return "Overweight"
        elif bmi > 30.0:
            return "Obesity"

    def print_self(self):
        print("""
first name: {0} 
last name: {1} 
weight in lbs: {2} 
height in inches: {3}
bmi: {4}
my bmi meaning: {5}""".format(
            self.first_name,
            self.last_name,
            self.weight_in_lbs,
            self.height_in_inches,
            self.calc_bmi(),
            self.bmi_range_checker()
        ))

    @classmethod
    def print_class(cls,):
        print("""
first name: {0} 
last name: {1} 
weight in lbs: {2} 
height in inches: {3}""".format(
            cls.first_name,
            cls.last_name,
            cls.weight_in_lbs,
            cls.height_in_inches
        ))
