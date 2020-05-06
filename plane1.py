import random


class Plane:
    def _init_(self, begin=0):
        self.begin = begin

    def tilt(self, degree):
        degree = random.randint(-90, 90)
        self.begin += degree

    def decompression(self, pressure_level: float = 1013, pressure_level_drop: float = random.random()):
         self.pressure_level = pressure_level

         if self.pressure_level == pressure_level - pressure_level_drop:
            return 'The oxygen masks had been released'


class Turbulance:

    def __init__(self, degree: float = 0):
        self.degree = degree

    def correction(self):
        number = random.random()
        self.degree = number

    def vibrations(self):
        number = random.gauss(0, 2 * random.randint(1, 10))
        self.degree = number
