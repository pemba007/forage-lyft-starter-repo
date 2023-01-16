from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        # Declaring Car
        self.__engine = engine
        self.__battery = battery

    def needs_service(self) -> bool:
        return self.__engine.needs_service() or self.__battery.needs_service()