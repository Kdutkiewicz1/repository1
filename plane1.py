import random
import time


class Plane:
    def _init_(self):
        self.begin = 0

    def tilt(self, degree):
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
        number = random.gauss(0, 2 * random.randint(1,10))
        self.degree = number


first_correction = 40
if __name__ == "__main__":
    plane = Plane()
    turbulence = Turbulance(0)
    end_program = 1



    while end_program == 1:
        time.sleep(1)
        turbulence.correction()
        turbulence.vibrations()
        print(turbulence.degree)
