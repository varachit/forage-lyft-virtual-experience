from abc import ABC
from datetime import datetime

from .battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date  # 27/07/22
        self.current_date = current_date  # 27/07/22 >= 27/07/25 ? True : False

    def needs_service(self) -> bool:
        # Task 1 and 2: Spindler Battery should be serviced once every 2 years
        # Task 3: Change to every 3 years
        return self.current_date >= self.addYears(self.last_service_date, 3)

    @staticmethod
    def addYears(original_date: datetime, years: int) -> datetime:
        return original_date.replace(year=original_date.year + years)
