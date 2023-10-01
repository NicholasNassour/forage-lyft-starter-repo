from battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        last_service_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        battery_needs_service = last_service_date < self.current_date
        if battery_needs_service:
            return True
        else:
            return False