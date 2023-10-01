from tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors
    
    def needs_service(self):
        return sum(self.tire_sensors) >= 3