import unittest
from datetime import date, datetime
from batteries.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date,today)
        return battery.needs_service()

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date,today)
        return battery.needs_service()