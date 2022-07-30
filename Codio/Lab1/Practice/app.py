from Person import *

p = Person("Tom", "Thumb", 150, 78)

print(Person)
print(p.first_name + " " + p.last_name + " weighs " + str(p.weight_in_lbs) + "lbs.")
print(p.calc_bmi())

p.first_name = "George"
print(p.first_name + " " + p.last_name + " weighs " + str(p.weight_in_lbs) + "lbs.")


p2 = Person('Fred', 'Flint', 225, 57)
print(p2.first_name + " " + p2.last_name + " weighs " + str(p2.weight_in_lbs) + "lbs.")
print(p2.calc_bmi())

print(Person.count)
print(Person.print_count())
