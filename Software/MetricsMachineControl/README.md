# MetricsMachineControl

![Default button setup](/images/MMLayout.gif)

## Install

Replace the ``main.py`` file on the KernTroller with the one found in this directory.

## Comments? Variable names?

File size is incredibly limited on the Trinket M0! To leave enough room for you to hack around with the the Python code and add more libraries, I tried to keep the text of the code as small as possible.

This means that there are almost no comments in the code, I used tab characters instead of spaces (honestly, it really saves data!) and variable names are as short as possible (``tBl`` instead of ``touchBlevel``, etc.).

To help you unerstand how the code works, I've also included a ``main-commented.py`` script that's functionally the same as the ``main.py`` that you would install on the device, except it's full of comments. It's still small enough to install, but it leaves less space for you to hack around and expand upon what's already there.

## Start up calibration

When you plug in the board, or when the board restarts after you've saved a code update, you'll notice a steady red light, and then two seconds of flsahing red lights. During the time that the lights are flashing, the code is taking a quick calibration test of the touch pads to figure out what the zero point is, so just keep your fingers off the touch pads! If you need to recalibrate, just unplug and replug the device.

![Calibration](/images/calibration.gif)

## How it works

The ``main-commented.py`` tells the full story, but generally speaking the code makes the KernTroller identify itself to your computer as if it was as keyboard, and each button on the KernTroller has its own "callback" function  (``cUp()``, ``cDown()``, etc.) toward the top of the script that fires off a keyboard command and sets the "dot" LED on the board to a color of your choosing.

The Trinket M0 only has five general purpose input/output pins, but the KernTroller has six "buttons" ("up" and "down" touch pads on your left hand, "A" and "B" touch pads on your right hand" and then two physical "L" and "R" buttons along the top). This required a clever hack: the "A" pad is connected to one input (pin 5), the "B" pad is connected to one input (pin 4), but the "up" and "down" pads are connected to two inputs (pin 3 and pin 1 for the "up", and pin 4 and pin 1 for the "down")

So, when a touch is detected the device still needs to wait a small moment (1/20th of a second in this case) to give enough time for it to detect if two inputs were actually touched at the same time.

Likewise, the "A" and "B" pads on their own are intended to read how firmly you've pressed down on the board. This 1/20th of a second is enough time to let your finger press as firmly as you intended it to, instead of having it fire off a keyboard command as soon as it sensed your touch.

## How to modify

The easiest things to modify are toward the top of the script:

#### Adjust the touch sensitivity

The ``lvls`` list defines the threshold levels for a very tiny touch, a medium sized touch, and a firm touch. If you find the touch pads are too sensitive or not sensitive enough, try adjusting these values. Be cautioned that if you set one item to ``0`` the button might constantly be on. 

#### Change the LED brightness

The ``lB`` variable sets the brighness of the RGB LED, set it to ``0`` if you're annoyed with all the LED blinking.

#### Change the keystrokes and LED color

Have a look at the [reference for the Adafruit HID Keyboard library](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode) for a list of all available keyboard keycodes. 

The callbacks toward the top of the script are where you can change how each key works: for instance ``k.press(Keycode.UP_ARROW)`` will fire off the keyboard command for an up arrow, ``k.press(Keycode.GUI, Keycode.G)`` will type command-G.
