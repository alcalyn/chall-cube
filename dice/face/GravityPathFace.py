from time import sleep
from .Face import Face


class GravityPathFace(Face):

    def __init__(self, accelerometer):
        self.accelerometer = accelerometer

    def start(self):
        self.display('Running gravity path face.')

        while True:
            current_face = self.accelerometer.get_current_face()

            self.display('Current face: %d' % current_face)

            sleep(0.8)
