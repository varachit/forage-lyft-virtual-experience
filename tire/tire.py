from abc import abstractmethod


class Tire:
    @abstractmethod
    def needs_service(self):
        pass
