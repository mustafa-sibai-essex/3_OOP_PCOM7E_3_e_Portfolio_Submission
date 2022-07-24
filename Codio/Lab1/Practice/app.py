from Person import *

p = Person("Tom", "Thumb", 150, 78)

print(Person)
print(p.first_name + " " + p.last_name + " weighs " + str(p.weight_in_lbs) + "lbs.")

p.first_name = "George"

print(p.first_name + " " + p.last_name + " weighs " + str(p.weight_in_lbs) + "lbs.")
