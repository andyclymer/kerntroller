# KernTroller Software

When you connect the KernTroller (or rather the Adafruit Trinket M0) to your computer you'll find that it mounts as a small ``CIRCUITPY`` drive. Each time the Trinket M0 is powered up or restarted it will run the ``main.py`` that it finds at the root level of its file system, so all of your code editing will start with this file. I've included a few preset Python scripts that you can drop in and start using.

The Trinket M0 is a full 32-bit computer, but resources are scarce! With only 256k of storage, after embedding a slimmed down Python standard library there isn't much room left for your own code. 

In my examples you'll find that in an effort to eke out as much code as possible I've left out comments, reduced variable names to be as short as possible, and am using tabs instead of spaces for whitespace (1/3 the characters!)

So, alongside each Python script that you would install on the device, I'll sometimes also include another version that's functinoally the same but includes all of the comments you need to know how it all works.


## Start by updating CircuitPython

If you're building KernTroller yourself, before you get too far you will most likely need to update the version of CircuitPython that comes on the Trinket M0.

To update CircuitPython, you can follow [the updating instructions provided by Adafruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython), or follow my summary here —

* Go to the [latest release page on the CircuitPython repository](https://github.com/adafruit/circuitpython/releases/latest)
* Locate and download the build for the Trinket M0, its file name will look something like:
  * ``adafruit-circuitpython-trinket_m0-?.?.?.uf2``
* Connect the Trinket to your computer with a USB cable, if it wasn't already.
* On the Trinket you'll find a small "Reset" button, tap this button twice to make it reboot into the bootloader.
* A new "TRINKETBOOT" drive will mount on your desktop — simply copy the file you downloaded in a previous step onto this drive to install.
* The Trinket will reboot once again, this time with the latest version of CircuitPython.


## Debug

A simple debug script to print bar graphs of the touch sensor and button status to the terminal to make sure that everything is working once you've finished the build.


## MetricsMachineControl

The default setup, ready to control Metrics Machine.

Have a look at the comments to see how it all works, but you're free to edit the code to adjust the sensitivity of the touch pads, and to configure different keystrokes of the virtual keyboard with each button press.x
