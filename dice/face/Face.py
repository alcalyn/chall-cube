class Face:

    def __init__(self):
        self.face_number = None

    def get_face_number(self):
        return self.face_number

    def set_face_number(self, face_number):
        self.face_number = face_number

        return self

    def display(self, message):
        print("Face %d: %s" % (self.get_face_number(), message))

    def start(self):
        self.display('Face starting')
