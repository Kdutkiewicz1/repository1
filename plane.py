import logging
from plane1 import Plane
from abc import ABC, abstractmethod
import random
import multiprocessing as mp


class Event(ABC):

    def __init__(self):
        self.tilt = random.randint(1, 90)
        super().__init__()

    @abstractmethod
    def change_tilt(self):
        pass


class Turbulance(Event):
    def change_tilt(self):
        return self.tilt


class Correction(Event):
      def change_tilt(self):
          corect = random.gauss(0, 2 * random.randint(1, 10))
          self.tilt = corect
          return self.tilt


def main():
    plane = Plane()
    turbu = Turbulance()
    corr = Correction()
    logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(message)s')
    logging.info('Corect angle:{}'.format(plane.begin))
    plane.tilt(turbu.change_tilt())
    logging.warning('Turbulance:{}'.format(turbu.change_tilt()))
    plane.tilt(corr.change_tilt())
    logging.info('Correction:{}'.format(corr.change_tilt()))


if __name__ == "__main__":
    processes = [mp.Process(target=main()) for x in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

