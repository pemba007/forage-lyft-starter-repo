from .tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, sensors):
        self.__sensors = sensors

    def needs_service(self) -> bool:
        return any(i >= 0.9 for i in self.__sensors)