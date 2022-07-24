from Person import *

p1 = Person("Tom", "Thumb", 120, 155)
p2 = Person("Fred", "Daniel", 100, 173)
p3 = Person("George", "Dunn", 80, 188)
p4 = Person("Tanya", "Mcfarlane", 70, 171)
p5 = Person("Mary", "Arnold", 125, 180)

people = [p1, p2, p3, p4, p5]

for person in people:
    print(person.first_name)
