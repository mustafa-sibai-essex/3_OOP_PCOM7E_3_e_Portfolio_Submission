class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print("{0}:{1}:{2}".format(time.hour, time.minute, time.second))