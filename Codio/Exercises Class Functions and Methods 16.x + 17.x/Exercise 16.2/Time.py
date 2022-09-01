class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def add_time(t1: Time, t2: Time):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


def print_time(time_obj: Time):
    print(
        "{:02d}:{:02d}:{:02d}".format(time_obj.hour, time_obj.minute, time_obj.second)
    )
