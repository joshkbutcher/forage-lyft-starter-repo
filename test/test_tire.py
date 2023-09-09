import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_tire_needs_serviced(self):
        wear = [0, 1.0, 0.9, 0.6]

        tire = CarriganTire(wear)
        self.assertTrue(tire.needs_service())

    def test_tire_doesnt_need_serviced(self):
        wear = [0, 0.8, 0.5, 0.6]

        tire = CarriganTire(wear)
        self.assertFalse(tire.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_needs_serviced(self):
        wear = [1.0, 1.0, 0.9, 0.6]

        tire = OctoprimeTire(wear)
        self.assertTrue(tire.needs_service())

    def test_tire_doesnt_need_serviced(self):
        wear = [0, 0.8, 0.5, 0.6]

        tire = OctoprimeTire(wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()