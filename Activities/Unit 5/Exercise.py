class Sensor:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

    def print_info(self):
        print(
            "Sensor info: name: {0}, frequency: {1}".format(self.name, self.frequency)
        )

    def start(self):
        print("Sensor is starting")


class ProximitySensor(Sensor):
    def __init__(self, name, frequency):
        super().__init__(name, frequency)

    def print_info(self):
        print(
            "Proximity Sensor: name: {0}, frequency: {1}".format(
                self.name, self.frequency
            )
        )

    def start(self):
        print("Proximity Sensor is starting")


class OxygenSensor(Sensor):
    def __init__(self, name, frequency):
        super().__init__(name, frequency)

    def print_info(self):
        print(
            "Oxygen Sensor: name: {0}, frequency: {1}".format(self.name, self.frequency)
        )

    def start(self):
        print("Oxygen Sensor is starting")


objects = [ProximitySensor("Proximity", 1000), OxygenSensor("Oxygen", 2000)]

for sensor in objects:
    sensor.print_info()
    sensor.start()
