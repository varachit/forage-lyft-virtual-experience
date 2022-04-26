from abc import ABC
from datetime import datetime

from .battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Nubbin Battery should be serviced once every 4 years
        return self.current_date >= self.addYears(self.last_service_date, 4)

    @staticmethod
    def addYears(original_date: datetime, years: int) -> datetime:
        return original_date.replace(year=original_date.year + years)
