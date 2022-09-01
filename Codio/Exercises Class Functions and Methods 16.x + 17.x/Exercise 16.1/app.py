from Time import *

t1 = Time(11, 59, 30)
t2 = Time(2, 30, 0)

print_time(t1)
print(is_after(t1, t2))

race_time = Time()
race_time.hour = 3
race_time.minute = 34
race_time.second = 5

avarage_time = end_race(race_time, 26.2)
print("%.2d:%.2d:%.2d per mile" % (avarage_time.hour, avarage_time.minute, avarage_time.second))
