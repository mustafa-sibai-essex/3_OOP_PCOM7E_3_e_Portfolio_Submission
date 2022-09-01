class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def mul_time(time_obj: Time, number: int):
    time_int = time_to_int(time_obj) * number
    new_time = int_to_time(time_int)
    if new_time.hour > 12:
        new_time.hour = new_time.hour % 12
    return new_time


def end_race(time_obj: Time, distance):
    """
    Returns time object that represents the average pace (time per mile) 
    time_obj: Time object
    distance: distance
    """
    return mul_time(time_obj, (1.0 / distance))


def print_time(time_obj: Time):
    """
    Prints a string representation of the time.
    time_obj: Time object
    """
    print(
        "{:02d}:{:02d}:{:02d}".format(time_obj.hour, time_obj.minute, time_obj.second)
    )


def is_after(t1: Time, t2: Time):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
