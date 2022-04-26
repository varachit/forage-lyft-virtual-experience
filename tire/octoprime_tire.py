from functools import reduce

from .tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        summation = reduce(lambda x, y: x + y, self.sensor)
        return summation >= 3
