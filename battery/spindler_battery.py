from abc import ABC
from car import Car
from datetime import datetime



class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        self.current_date = datetime.today().date()

    def battery_should_be_serviced(self):
        if self.service_threshold_date.year < self.current_date.year:
            return True
        else:
            return False

