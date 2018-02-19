import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar


"""
~~~~~~~~~~~~~~~~~~
Kern>troller Debug
~~~~~~~~~~~~~~~~~~

Prints bar graphs to show values for touch pads and L/R buttons

    A @@@@@@@------------- B @@@@@@@@------------ C @@@@@@@@@@@@@@@----- LLL RRR

Find the port name for the device by listing the contents of /dev/tty.*
    ls /dev/tty.*

Connect to the device, replace 0000 with the port number found above:
    screen /dev/tty.usbmodem0000

Detach from the "screen" command with control-a followed by control-d

"""

# dotstar LED
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)


# Digital input with pulldown
buttonR = DigitalInOut(board.D2)
buttonR.direction = Direction.INPUT
buttonR.pull = Pull.DOWN

buttonL = DigitalInOut(board.D0)
buttonL.direction = Direction.INPUT
buttonL.pull = Pull.DOWN

# Capacitive touch on D3
touchA = touchio.TouchIn(board.D3)
touchB = touchio.TouchIn(board.D4)
touchC = touchio.TouchIn(board.D1)


while True:
    # Touch level bar graph
    tAv = int(round(touchA.raw_value / 204))
    tBv = int(round(touchB.raw_value / 204))
    tCv = int(round(touchC.raw_value / 204))
    tAs = "@" * tAv
    tAs += "-" * (20 - tAv)
    tBs = "@" * tBv
    tBs += "-" * (20 - tBv)
    tCs = "@" * tCv
    tCs += "-" * (20 - tCv)
    # L/R button
    if buttonL.value:
        lv = "LLL"
    else: lv = ".l."
    if buttonR.value:
        rv = "RRR"
    else: rv = ".r."
    print("A", tAs, "B", tBs, "C", tCs, lv, rv)

