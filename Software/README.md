# KernTroller Software

When you connect the KernTroller (or rather the Adafruit Trinket M0) to your computer you'll find that it mounts as a small ``CIRCUITPY`` drive. Each time the Trinket M0 is powered up or restarted it will run the ``main.py`` that it finds at the root level of its file system, so all of your code editing will start with this file. I've included a few preset Python scripts that you can drop in and start using.

The Trinket M0 is a full 32-bit computer, but resources are scarce! With only 256k of storage, after embedding a slimmed down Python standard library there isn't much room left for your own code. 

In my examples you'll find that in an effort to eke out as much code as possible I've left out comments, reduced variable names to be as short as possible, and am using tabs instead of spaces for whitespace (1/3 the characters!)

So, alongside each Python script that you would install on the device, I'll sometimes also include another version that's functinoally the same but includes all of the comments you need to know how it all works.


## Debug

A simple debug script to print bar graphs of the touch sensor and button status to the terminal to make sure that everything is working once you've finished the build.


## MetricsMachineControl

The default setup, ready to control Metrics Machine.

Have a look at the comments to see how it all works, but you're free to edit the code to adjust the sensitivity of the touch pads, and to configure different keystrokes of the virtual keyboard with each button press.x
