import unittest

from Car.tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprime(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        sensorData = [1.1, 0.5,0.7,0.8]

        tyre = OctoprimeTyre(sensors=sensorData)
    
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        sensorData = [0.0, 0.5, 0.7, 0.9]

        tyre = OctoprimeTyre(sensors=sensorData)
    
        self.assertFalse(tyre.needs_service())