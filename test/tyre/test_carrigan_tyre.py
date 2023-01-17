import unittest

from Car.tyre.carrigan_tyre import CarriganTyre

class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        sensorData = [0.0, 0.5,0.7,0.9]

        tyre = CarriganTyre(sensors=sensorData)
    
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        sensorData = [0.0, 0.5, 0.7,0.8]

        tyre = CarriganTyre(sensors=sensorData)
    
        self.assertFalse(tyre.needs_service())