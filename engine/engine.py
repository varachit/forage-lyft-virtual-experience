from abc import abstractmethod


class Engine:
    @abstractmethod
    def engine_should_be_serviced(self):
        pass
