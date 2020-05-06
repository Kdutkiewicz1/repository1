import logging
import multiprocessing as mp
from jhhjhjssdsd import Plane
from abc import ABC, abstractmethod
import random


class Event(ABC):

    def __init__(self):
        self.degree = random.randint(1, 90)
        super().__init__()

    @abstractmethod
    def change_degree(self):
        pass


class Turbulance(Event):
    def change_degree(self):
        return self.degree


class Correction(Event):

    def change_degree(self):
        value = random.gauss(0, 2 * random.randint(1, 9))
        self.degree = value
        return self.degree


def main():
     plane = Plane()
     turbulence = Turbulance()
     corr = Correction()
     logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO, format ='%(asctime)s %(message)s')
     logging.info('plane orientation {} '.format(plane.begin))
     plane.tilt(turbulence.change_degree())
     logging.warning('plane orientation after turbulance {} '.format(plane.begin))
     plane.tilt(corr.change_degree())
     logging.warning('plane orientation after correction {}'.format(plane.begin))

if __name__ == "__main__":
     processes = [mp.Process(target=main()) for x in range(10)]
     for p in processes:
       p.start()
     for p in processes:
       p.join()

