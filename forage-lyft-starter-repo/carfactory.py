from car import Car
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from nubbin_battery import NubbinBattery

class CarFactory(Car):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

