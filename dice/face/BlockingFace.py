from time import sleep
from .Face import Face


class BlockingFace(Face):

    def __init__(self, time=3):
        self.time = time

    def start(self):
        self.display('Face running %d seconds...' % self.time)
        sleep(self.time)
        self.display('End of %d seconds.' % self.time)
