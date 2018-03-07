# Debug

The debug script prints out a simple bar graph of the touch sensor and button state to the terminal, to check if everything is working correctly after building.

## Install

Replace the ``main.py`` file on the KernTroller with the one found in this directory.

## How to use

The Python script is executed entirely on the Trinket M0 attached to the KernTroller, you can open up a Terminal "screen" to remotely connect to the device to look in on any Python tracebacks as they happen, or any standard output that would come from a ``print()`` statement.

After installing the ``main.py``, find the device's port number with the following terminal command:

```
ls /dev/tty.*
```

Every USB port on your computer has a different serial address, the port name that you're looking for should probably be in the format that looks like ``tty.usbmodem1441``

To try to open a "screen" for your Trinket, use the following command in the Terminal, replacing the "????" with the port number that you found in the previous step:

```
screen /dev/tty.usbmodem1441
```

If this didn't work, and if you found more than one "usbmodem" port names, try another.

If it did work, you should see an output of the current state of the buttons on your KernTroller:

```
 A @@@@@@@------------- B @@@@@@@@@----------- C @@@@@@@@@----------- .l. RRR
 A @@@@@@@@@----------- B @@@@@@@@------------ C @@@@@@@@@----------- .l. RRR
 A @@@@@@@@@@@--------- B @@@@@@@@------------ C @@@@@@@@@----------- .l. .r.
 A @@@@@@@@@@@@-------- B @@@@@@@@------------ C @@@@@@@@@----------- .l. .r.
 A @@@@@@@@@@@@-------- B @@@@@@@@@----------- C @@@@@@@@@----------- LLL .r.
 A @@@@@@@@@@@--------- B @@@@@@@@@@@--------- C @@@@@@@@@----------- LLL .r.
 A @@@@@@@------------- B @@@@@@@@@@@@@------- C @@@@@@@@@----------- LLL .r.
```

Notice that even when you're not pressing on a touch pad it always has some reading, often even at 50%! Because of this, if you're going to write a script that needs to know the zero value for the touch sensors it's important to take a quick calibration reading of the default touch pad values. For an example, have a look at how the "MetricsMachineControl".

To exit the "screen", type ``control-a`` and then ``control-d`` to "detach" from the screen.
