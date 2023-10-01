from tire import Tire

class CarriganTires(Tire):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors
    
    def needs_service(self):
        return max(self.tire_sensors) >= 0.9