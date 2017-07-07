from time import sleep
from .Face import Face


class BlockingFace(Face):

    def __init__(self, time=3):
        self.time = time

    def start(self):
        print('Face running %d seconds...' % self.time)
        sleep(self.time)
        print('End of %d seconds.' % self.time)
