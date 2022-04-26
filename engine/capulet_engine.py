from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def engine_should_be_serviced(self):
        # If the current mile age exceeds 30,000 miles, it should be serviced
        return self.current_mileage - self.last_service_mileage > 30000
