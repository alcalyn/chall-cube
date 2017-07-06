from dice.sensor.Accelerometer import Accelerometer
from dice.face.BlankFace import BlankFace
from dice.face.BlockingFace import BlockingFace
from dice.face.GravityPathFace import GravityPathFace
from dice.Dice import Dice

accelerometer = Accelerometer()

faces = [
    BlankFace(),
    BlockingFace(),
    BlankFace(),
    BlankFace(),
    GravityPathFace(accelerometer),
    BlankFace()
]

dice = Dice(faces)

dice.start()
