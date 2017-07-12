Challenge Cube
==============

Base API for RaspberryPi Cube.

Cube is physical, and has 6 faces, all drived by Raspberry Pi.
Each face is a challenge, has some electronic elements programmatically drived by a `Face` python class.

This library provides a base class `Face` to implement a challenge, and then run all 6 faces asynchronously.

It also provides Cube devices API, like accelerometer to know which face is up.


## Installation

``` bash
pip install chall_cube
```


## Usage

### Testing with base faces

Implement a cube with 6 blank faces which do nothing:

``` python
from chall_cube.Cube import Cube
from chall_cube.face.BlankFace import BlankFace

faces = [
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace()
]

dice = Cube(faces)

dice.start()
```

Test to blink a led wired on pin 18 on the face with the class `BlinkingFace`:

``` python
from chall_cube.Cube import Cube
from chall_cube.face.BlinkingFace import BlinkingFace

faces = [
    # ...
    BlinkingFace(18)
]

dice = Cube(faces)

dice.start()
```


### Implement a custom face

When the cube starts, it calls the `start` method from all its faces.

**Face which does nothing**:

``` python
from chall_cube.face.Face import Face


class MyCustomFace(Face):

    def start(self):
        self.print('My custom face is running.')
        # Face logic here, light on leds, use cube API...
```

`self.print` method will print logs on terminal prefixed with the face unique name.
Used to identify which face is logging.

To integrate this custom face to the cube, just add it to a `Cube` instance.

**Integrating custom face to cube**:

``` python
from chall_cube.Cube import Cube
from chall_cube.face.BlankFace import BlankFace

faces = [
    MyCustomFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace()
]

dice = Cube(faces)

dice.start()
```

This library provides some basic faces, like `BlankFace` which does nothing.

It also provides `BlinkingFace`, that just makes blinking a led. It can be used to test the cube.

**Blinking a led wired on pin 18**:

``` python
from time import sleep
from chall_cube.face.Face import Face
from gpiocrust import Header, OutputPin


class MyCustomFace(Face):

    def start(self):
        with Header():
            pin = OutputPin(18)

            while True:
                self.print('Pin ON')
                pin.value = 1
                sleep(1)

                self.print('Pin OFF')
                pin.value = 0
                sleep(1)
```

Note that this thread is blocking, because in a `while True` loop.

It becomes a problem when you want to quit the cube process with `CTRL+C`:
you'll have to `CTRL+C` twice to force quit the process.

To avoid this, and softly stop the face process, you can listen to cube **stop request**,
then break the loop.

**Listen to cube stop request**:

``` python
from time import sleep
from chall_cube.face.Face import Face
from gpiocrust import Header, OutputPin


class MyCustomFace(Face):

    def __init__(self):
        super().__init__()

        self.__has_stop_request = False

    def request_stop(self):
        self.__has_stop_request = True

    def start(self):
        with Header():
            pin = OutputPin(18)

            while not self.__has_stop_request:
                self.print('Pin ON')
                pin.value = 1
                sleep(1)

                self.print('Pin OFF')
                pin.value = 0
                sleep(1)
```

The method `request_stop` is called by the cube when it want to stop.

In this example, the loop breaks after 2 seconds max after the stop request,
and avoid to force stop the face challenge.


### Cube devices API

The cube API provides devices API, such as accelerometer.


#### Accelerometer

Accelerometer provides the current cube orientation.

It is useful to know which face is up.

``` python
from chall_cube.device.Accelerometer import Accelerometer

accelerometer = Accelerometer()

accelerometer.get_current_face()
# Returns an integer from 1 to 6
```


## License

This library is under [AGPL-3.0 License](LICENSE).
