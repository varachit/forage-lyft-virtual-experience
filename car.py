from abc import abstractmethod
from engine.engine import Engine
from battery.battery import Battery


class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
