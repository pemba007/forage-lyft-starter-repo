from .tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, sensors):
        self.__sensors = sensors

    def needs_service(self) -> bool:
        return sum(self.__sensors) >= 3