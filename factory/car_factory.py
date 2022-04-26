from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensor) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor)
        calliope = Car(engine, battery, tire)
        return calliope

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensor) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor)
        glissade = Car(engine, battery, tire)
        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, sensor) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor)
        palindrome = Car(engine, battery, tire)
        return palindrome

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensor) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(sensor)
        rorschach = Car(engine, battery, tire)
        return rorschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensor) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensor)
        thovex = Car(engine, battery, tire)
        return thovex
