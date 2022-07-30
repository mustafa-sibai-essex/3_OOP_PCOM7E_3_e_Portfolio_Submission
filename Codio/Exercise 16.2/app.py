from Time import *
from datetime import datetime

t1 = Time(11, 59, 30)
t2 = Time(2, 0, 0)
sum_t1_and_t2 = add_time(t1, t2)

print_time(t1)
print_time(t2)
print_time(sum_t1_and_t2)

# 1.Use the datetime module to write a program that gets the current date
# and prints the day of the week.

current_date = datetime.today()
print("Current Date is: {0}".format(current_date))
print("Today is: {0}".format(current_date.strftime("%A")))


# 2.Write a program that takes a birthday as input and prints the user’s age and
# the number of days, hours, minutes and seconds until their next birthday.

birth_date_str = '5/08/1992'
birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
next_birth_date = birth_date.replace(year=current_date.year)

if next_birth_date < current_date:
    next_birth_date = next_birth_date.replace(year=current_date.year + 1)

print("Your birth date is on: {0}".format(birth_date))
print("Your next birth date is on: {0}".format(next_birth_date))

time_until_next_birth_date = next_birth_date - current_date
print("{0} until your next birth date".format(time_until_next_birth_date))

last_birth_date = next_birth_date.replace(year=next_birth_date.year - 1)
age = last_birth_date.year - birth_date.year
print("You are {0} years old".format(age))

next_age = next_birth_date.year - birth_date.year
print("In {0} you will be {1} years old".format(time_until_next_birth_date, next_age))


# 3.For two people born on different days, there is a day when one is
# twice as old as the other. That’s their Double Day.
# Write a program that takes two birthdays and computes their Double Day.

birth_date_1_str = '11/05/1998'
birth_date_1 = datetime.strptime(birth_date_1_str, '%d/%m/%Y')

birth_date_2_str = '5/08/1992'
birth_date_2 = datetime.strptime(birth_date_2_str, '%d/%m/%Y')

print("For two people born on different days, there is a day when one is twice as old as the other")
print("birth date 1: {0}".format(birth_date_1))
print("birth date 2: {0}".format(birth_date_2))

oldest = min(birth_date_1, birth_date_2)
youngest = max(birth_date_1, birth_date_2)
age_differance = youngest - oldest
double_day = youngest + age_differance

oldest_age = double_day.year - oldest.year
print("Person born on {0} will be {1} on {2}".format(oldest, oldest_age, double_day))

youngest_age = double_day.year - youngest.year
print("Person born on {0} will be {1} on {2}".format(youngest, youngest_age, double_day))
