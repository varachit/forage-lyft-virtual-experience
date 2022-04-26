from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        for each_data in self.sensor:
            if each_data >= 0.9:
                return True
        return False
