import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_sensor = [0.6, 0.89, 0.89, 0.89]
        tires = OctoprimeTires(tire_sensor)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_sensor = [0.1, 0.2, 0.3, 0.6]
        tires = OctoprimeTires(tire_sensor)
        self.assertTrue(tires.needs_service())