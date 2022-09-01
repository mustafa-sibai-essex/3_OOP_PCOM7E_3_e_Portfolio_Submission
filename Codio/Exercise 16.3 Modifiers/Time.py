class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def increment(time, seconds):

    t = Time(time.hour, time.minute, time.second)
    t.second += seconds

    if t.second >= 60:
        t.second -= 60
        t.minute += 1

    if t.minute >= 60:
        t.minute -= 60
        t.hour += 1

    return t


def print_time(time_obj: Time):
    print(
        "{:02d}:{:02d}:{:02d}".format(time_obj.hour, time_obj.minute, time_obj.second)
    )
