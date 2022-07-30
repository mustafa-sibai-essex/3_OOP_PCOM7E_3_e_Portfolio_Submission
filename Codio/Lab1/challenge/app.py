from Person import *

Person.first_name = "Mustafa"
Person.last_name = "Sibai"
Person.weight_in_lbs = 120
Person.height_in_inches = 71

Person.print_class()

p1 = Person("Tom", "Thumb", 110, 65.78)
p2 = Person("Fred", "Daniel", 168, 71.52)
p3 = Person("George", "Dunn", 170, 69.40)
p4 = Person("Tanya", "Mcfarlane", 205, 68.22)
p5 = Person("Mary", "Arnold", 190, 67.79)

people = [p1, p2, p3, p4, p5]

for person in people:
    person.print_self()

Person.print_class()
