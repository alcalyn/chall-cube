from threading import Thread


class Cube:

    def __init__(self, faces):
        self.faces = faces
        self.threads = []

    def start(self):
        self.threads = []

        for face_number, face in enumerate(self.faces, start=1):
            thread = Thread(target=face.start)

            thread.start()

            self.threads.append(thread)
