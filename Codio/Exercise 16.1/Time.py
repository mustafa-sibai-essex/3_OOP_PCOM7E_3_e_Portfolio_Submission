class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def print_time(time_obj: Time):
    print(
        "{:02d}:{:02d}:{:02d}".format(time_obj.hour, time_obj.minute, time_obj.second)
    )


def is_after(t1: Time, t2: Time):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
