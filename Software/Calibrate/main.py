import os
import board
import time
import touchio


"""
Kern>Troller Calibration

First, the latest version of CircuitPython:
	https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

Find the device's port number:
	ls /dev/tty.*

Connect to the device, replace ???? with the port number:
	screen /dev/tty.usbmodem????

Every 5 seconds, the terminal will display an updated minimum value for the touch sensors.

	Don't touch the touch pads while it's measuring the minimum value !!!

These three values can be copied and pasted into the script of your choosing,
replace the default values that you find with the data that matches your device


"""

touchA = touchio.TouchIn(board.D3)
touchB = touchio.TouchIn(board.D4)
touchC = touchio.TouchIn(board.D1)


while True:
	
	print("-"*20)
	sTime = time.monotonic()
	# Record highest and lowest readings
	rA = [4094, 0]
	rB = [4094, 0]
	rC = [4094, 0]
	t = 5 # sample time
	while sTime + t >= time.monotonic():
		vA = touchA.raw_value
		if vA < rA[0]: rA[0] = vA
		elif vA > rA[1]: rA[1] = vA
		vB = touchB.raw_value
		if vB < rB[0]: rB[0] = vB
		elif vB > rB[1]: rB[1] = vB
		vC = touchC.raw_value
		if vC < rC[0]: rC[0] = vC
		elif vC > rC[1]: rC[1] = vC
	# Minimum floor is low+(high-low)*2 to kick it up a little bit to be safe
	tA = rA[0] + (rA[1] - rA[0]) * 2
	tB = rB[0] + (rB[1] - rB[0]) * 2
	tC = rC[0] + (rC[1] - rC[0]) * 2
	# Print the data
	cal = "minA = %s\nminB = %s\nminC = %s" % (tA, tB, tC)
	print(cal)