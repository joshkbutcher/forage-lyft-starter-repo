import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_car_needs_serviced(self):
        current_mileage = 40000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_car_doesnt_need_serviced(self):
        current_mileage = 25000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestSternman(unittest.TestCase):
    def test_car_needs_serviced(self):
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_car_doesnt_need_serviced(self):
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_car_needs_serviced(self):
        current_mileage = 65000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_car_doesnt_need_serviced(self):
        current_mileage = 50000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestNubbin(unittest.TestCase):
    def test_battery_needs_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_need_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):
    def test_battery_needs_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_need_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
