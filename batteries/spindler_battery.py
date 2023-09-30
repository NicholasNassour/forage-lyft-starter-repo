from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
    
    def needs_service(self):
        return self.last_service_date - self.current_date > 2