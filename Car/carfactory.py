from car import Car
from datetime import date
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import NubbinBattery, SpindlerBattery

class CarFactory:
    # def __init__(self):
    #     print("Hello CarFactory")

    # Factory methods

    # Callipoe Car
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Capulet Engine & Spindler Battery
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)

        return Car(engine=engine, battery=battery)
    
    # Glissade Car
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        
        # Willoughby Engine & Spindler Battery
        engine = WilloughbyEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        
        return Car(engine=engine, battery=battery)

    # Palindrome Car
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:

        # Sternman Engine & Spindler Battery
        engine = SternmanEngine(warning_light_is_on= warning_light_on)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)
    
    # Rorschach Car
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Willoughby Engine & Nubbin Battery
        engine = WilloughbyEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = NubbinBattery(last_service_date= last_service_date, current_date= current_date)

        return Car(engine=engine, battery=battery)

    # Thovex Car
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Capulet Engine & Nubbin Battery
        engine = CapuletEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = NubbinBattery(last_service_date= last_service_date, current_date= current_date)
        
        return Car(engine=engine, battery=battery)