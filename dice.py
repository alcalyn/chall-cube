from cube.sensor.Accelerometer import Accelerometer
from cube.face.BlankFace import BlankFace
from cube.face.BlockingFace import BlockingFace
from cube.face.GravityPathFace import GravityPathFace
from cube.Cube import Cube

accelerometer = Accelerometer()

faces = [
    BlankFace(),
    BlockingFace(),
    BlankFace(),
    BlankFace(),
    GravityPathFace(accelerometer),
    BlankFace()
]

dice = Cube(faces)

dice.start()
