import logging
import multiprocessing as mp
from plane1 import Turbulance, Plane
from abc import ABC, abstractmethod
import random


class Event(ABC):

    def __init__(self):
        self.angle = random.randint(1, 40)
        super().__init__()

    @abstractmethod
    def degree(self):
        pass

def main():
          plane = Plane()
          turbulence = Turbulance()
          logging.basicConfig(filename='information.log', filemode='w', level=logging.INFO,
          format='%(asctime)s %(message)s')
          logging.info('plane  inizial orientation {} '.format(plane.begin))
          plane.tilt(turbulence.correction())
          logging.warning('plane orientation after turbolance {} '.format(plane.begin))
          plane.tilt(turbulence.vibrations())
          logging.warning('plane orientation after correction {}'.format(plane.begin))


          if __name__ == "__main__":
             processes = [mp.Process(target=main()) for x in range(10)]
             for p in processes:
                 p.start()
             for p in processes:
                 p.join()
