class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def print_time(time_obj: Time):
    print(
        "{:02d}:{:02d}:{:02d}".format(time_obj.hour, time_obj.minute, time_obj.second)
    )
