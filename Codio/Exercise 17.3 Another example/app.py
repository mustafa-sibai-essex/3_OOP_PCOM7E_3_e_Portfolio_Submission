from Time import *

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()

end = start.increment(1337)
end.print_time()