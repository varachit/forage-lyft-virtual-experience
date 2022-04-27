import unittest
import sys
import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.getcwd())
sys.path.append(ROOT_DIR)

from factory.car_factory import CarFactory
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_calliope(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_calliope(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 25000
        last_service_mileage = 15000
        tire_sensor = [0.25, 0.8, 0.1, 0.9, 0.12]

        car = CarFactory.create_calliope(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 25000
        last_service_mileage = 15000
        tire_sensor = [0.74, 0.41, 0.06, 0.15, 0.2]

        car = CarFactory.create_calliope(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_glissade(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_glissade(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_glissade(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory.create_glissade(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 25000
        last_service_mileage = 15000
        tire_sensor = [0.7, 0.05, 0.11, 0.22, 0.91]

        car = CarFactory.create_glissade(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 25000
        last_service_mileage = 15000
        tire_sensor = [0.55, 0.31, 0, 0.1, 0.66]

        car = CarFactory.create_glissade(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_is_on = False
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor = [0.93, 0.7, 0, 0.64, 0.05]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor = [0, 0.79, 0, 0.18, 0.75]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_sensor)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_rorschach(current_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_rorschach(current_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_rorschach(last_service_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_rorschach(last_service_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 35000
        last_service_mileage = 25000
        tire_sensor = [0.84, 0.74, 0.44, 0.56, 0.99]

        car = CarFactory().create_rorschach(last_service_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 35000
        last_service_mileage = 25000
        tire_sensor = [0.02, 0.46, 0.13, 0.7, 0.15]

        car = CarFactory().create_rorschach(last_service_date, last_service_date,
                                            current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_thovex(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_thovex(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_thovex(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor = [0, 0, 0, 0, 0]

        car = CarFactory().create_thovex(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor = [0.97, 0.87, 0.61, 0.75, 0.41]

        car = CarFactory().create_thovex(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor = [0.14, 0.48, 0.24, 0.01, 0.3]

        car = CarFactory().create_thovex(last_service_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_sensor)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main(exit=False)
