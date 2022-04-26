from engine.engine import Engine
from battery.battery import Battery


class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.engine_should_be_serviced() or self.battery.needs_service()
