import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_sensor = [0.1, 0.2, 0.3, 0.9]
        tires = CarriganTires(tire_sensor)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_sensor = [0.1, 0.2, 0.3, 0.6]
        tires = CarriganTires(tire_sensor)
        self.assertTrue(tires.needs_service())