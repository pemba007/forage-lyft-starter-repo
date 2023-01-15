from abc import ABC, abstractmethod
from serviceable import Serviceable
from .Car.battery import Battery
from .Car.engine import Engine

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        # Declaring Car
        self.__engine = engine
        self.__battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        return self.__engine.needs_service() or self.__battery.needs_service()
