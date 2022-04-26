from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def engine_should_be_serviced(self) -> bool:
        # If the current mile age exceeds 60,000 miles, it should be serviced
        return self.current_mileage - self.last_service_mileage > 60000
