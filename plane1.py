import random
import time


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

    def vibrations(self, vibration: float):
        number = random.gauss(0, 2 * vibration)
        self.degree = number


first_correction = 40
if __name__ == "__main__":
    plane = Plane()
    turbulence = Turbulance(0)
    end_program = 1



    while end_program == 1:
        time.sleep(1)
        turbulence.correction()
        turbulence.vibrations(float(first_correction))
        print(turbulence.degree)
     
