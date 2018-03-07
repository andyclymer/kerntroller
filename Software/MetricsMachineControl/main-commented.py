import board
from digitalio import DigitalInOut, Direction, Pull
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_dotstar as dotstar
import time
import os


"""
Kern>troller
2018 Andy Clymer

	METRICS MACHINE SETTINGS
		# # # 'Commnented' Edition! # # #

Storage space is incredibly limited on the Trinket M0 so I would reocmmend that you use 
this version of the main.py as a reference, but that you install the uncommented version
so that you have enough room on the drive to add more Python. Otherwise, the two of these
are functinoally the same.

Note that in the comments I'll use the word "button" to refer to the physical buttons
but also to the touch pads, and I'll use the word "key" to refer to the actual keystrokes
that the KernTroller is sending to the computer (which could be more than one, for each
press of a button!)

"""

# Touch sensitivity levels
# These set the threshold for what makes a "light", "medium" or "firm" press of the "A" and "B" buttons
# Adjust these if you don't like the sensitivity of the buttons, but beware that setting one to 0 will
# likely result in a button always being "pressed down", or it might even trigger when your finger hasn't
# even touched the pad yet! (kinda cool actually...)
lvls = [0.07, 0.31, 0.43]

# LED brightness (a value between 0 and 1)
lB = 0.05


""" Callback Functions """

def cUP():
	""" Callback for the "Up" button: Previous Pair """
	print("Up")
	# Press the up arrow...
	k.press(Keycode.UP_ARROW)
	# ...and set the RGB led to 100% blue
	dot[0] = (0, 0, 255)

def cDOWN():
	""" Callback for the "Down" button: Next Pair """
	print("Down")
	k.press(Keycode.DOWN_ARROW)
	dot[0] = (0, 0, 255)

def cA(v):
	""" Callback for the "A" button: Negative Kern """
	# The strength of the touch value reading comes in as "v"
	# This next line is shorthand to turn the "v" level and the "tAl" or "threshold A levels" list
	# into an integer 1, 2 or 3 depending on which threshold was hit
	l = sum([v>=i for i in tAl]) 
	print("A", l)
	# Fire off a different keystroke depending on the level
	if l == 1: k.press(Keycode.ALT, Keycode.LEFT_ARROW)
	elif l == 2: k.press(Keycode.SHIFT, Keycode.LEFT_ARROW)
	elif l == 3: k.press(Keycode.LEFT_ARROW)
	dot[0] = (85*l, (l>2)*128, (l>1)*128)
	
def cB(v):
	""" Callback for the "B" button: Positive Kern """
	l = sum([v>=i for i in tBl])
	print("B", l)
	if l == 1: k.press(Keycode.ALT, Keycode.RIGHT_ARROW)
	elif l == 2: k.press(Keycode.SHIFT, Keycode.RIGHT_ARROW)
	elif l == 3: k.press(Keycode.RIGHT_ARROW)
	dot[0] = ((l>2)*128, 85*l, (l>1)*128)

def cMID():
	""" Callback for the "Middle" button: Unassigned """
	# There's a little hidden button at the bottom of the board just below the Trinket M0,
	# all it does right now is turn the LED to be yellow, but you can assign it to anything of your choosing
	print("Mid")
	dot[0] = (64, 64, 0)

def cL():
	""" Callback for the "Left" physical button: Show Glyph Stack"""
	k.press(Keycode.GUI, Keycode.G)
	print("L")
	led.value = 1

def cR():
	""" Callback for the "Right" physical buttonL Flip Pair """
	k.press(Keycode.GUI, Keycode.F)
	print("R")
	led.value = 1
	
def cbackRelease():
	""" Callback for when the buttons are released """
	k.release_all()
	dot[0] = (0, 0, 0)
	led.value = 0


""" Set up the board's input and output """
	
# Set up the "Dotstar" RGB LED on the Trinket M0 board
# They're designed to work in a sequence with a string of other LEDs,
# but since you only have one you'll just set the value for dot[0]
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=lB)
dot[0] = (0, 0, 0)

# Set up the Keyboard object
k = Keyboard()
kL = KeyboardLayoutUS(k)

# The "Right" physical button, or "bR", is wired up so that pressing down will
# make an electrical connection from pin D2 on the board to the 3.3v power connection.
# For this to work, set the pin D2 to be an Input, with an internal resistor pulling
# the pin down to the ground.
bR = DigitalInOut(board.D2)
bR.direction = Direction.INPUT
bR.pull = Pull.DOWN

# Same for the "Left" physical button, "bL", but this time on pin D0.
bL = DigitalInOut(board.D0)
bL.direction = Direction.INPUT
bL.pull = Pull.DOWN

# Initialize three touch pins
tA = touchio.TouchIn(board.D3)
tB = touchio.TouchIn(board.D4)
tC = touchio.TouchIn(board.D1)

# There's also another little red LED on the board aside from the RGB LED,
# it's on pin number D13.
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT


""" Calibrate the touch pads """

# Every board is different, and the capacitive touch pads even have slightly different readings
# depending on the weather it seems. So, calibrate them each time the board is started up
# to determine what the resting zero value us.

def calibrate():
	# Record the start time, and lists to populate with the minmum and maximum readings
	sTime = time.monotonic()
	rA = [4094, 0]
	rB = [4094, 0]
	rC = [4094, 0]
	# Time, number of seconds the full calibration routine should run for
	t = 4
	while sTime+t>=time.monotonic():
		# Turn the red led on...
		led.value = 1
		# ...and afte rone second start calibrating...
		if time.monotonic()-sTime>1:
			# the "f" value is used to blink the two LEDs on and off sequentially
			f = time.monotonic()%0.1 > 0.05 # this value will flip/flip every 1/20th o a second
			led.value = not f # off when the other led is on
			dot[0] = (f*255,0,0) # on RED when the other led is off
			# Take the raw value for each touch input.
			vA = tA.raw_value
			# If the value is lower than the lowest reading, save it.
			# If the value is higher than the highest reading, save it.
			if vA<rA[0]: rA[0]=vA
			elif vA>rA[1]: rA[1]=vA
			# Same for the other two touch pads...
			vB = tB.raw_value
			if vB<rB[0]: rB[0]=vB
			elif vB>rB[1]: rB[1]=vB
			vC = tC.raw_value
			if vC<rC[0]: rC[0]=vC
			elif vC>rC[1]: rC[1]=vC
	# The low and high readings help us determine how much noise the touch pads are picking up.
	# Take the difference between high and low values, to measure the amount of noise,
	# and set the minimum thresholds for the touch pads to be six times the noise value.
	# In my experience, this is enough to keep false triggering from happening.
	mA = rA[0]+(rA[1]-rA[0])*6
	mB = rB[0]+(rB[1]-rB[0])*6
	mC = rC[0]+(rC[1]-rC[0])*6
	# Done calibrating, turn the red LED off...
	led.value = 0
	# ...and turn the RGB LED green to show that calibration is done...
	dot[0] = (0,255,0)
	# ...but only for a quarter of a second...
	time.sleep(0.25)
	# ...before the LED turns to black.
	dot[0] = (0,0,0)
	print(mA,mB,mC)
	return mA,mB,mC
minA, minB, minC = calibrate()

# Using the minimum readings from the touch pads, and the "lvls" list of thresholds,
# pre-calculate the threshold levels for the three inputs.
# Since input "C" doesn't need a range of sensitivity (it's only used for the middle button
# and as the second touch pad for the "Up" and "Down" buttons", just give it a medium-ish threshold level.)
def vl(m, *l):
	return [m+((4096-m)*i) for i in l]
tAl = vl(minA, *lvls)
tBl = vl(minB, *lvls)
tCl = vl(minC, 0.4)[0]

""" Prepare to take button events! """

# Prepare a dictionary of the default button state, where each button has a state of zero.
# Dict values match the button names we've already been using
prev = dict(A=0, B=0, C=0, L=0, R=0)
# The time that the previous touch event happened, used for timing events.
# set it to the current time to get started
prevT = time.monotonic()
# The delay between when a touch is sensed and when its reading should be taken,
# in this case 1/20th of a second to give your finger enough time to touch the
# touch pad as firmly as you wanted it to, instead of firing off the callback
# the moment that the very first tip of your finger touched the pad
dly = 0.05
# Any keys currently active?
kActv = False
# While your finger is presing down on a touch pad, these variables will collect
# the highest level that was read during the event.
tAh = 0
tBh = 0

""" The main loop """

# Everything happens in a loop, aside from any outside functions. This "while True"
# will run forever until there's a traceback or the device is unplugged.
# Keep this in mind, this loop is running as fast as the little 48mhz device can run,
# so it's up to you to watch the time (prevT) if you want any event to happen 
# at a specific interval

while True:
	
	# Collect the current button state into a dictionary...
	st = dict(A=0, B=0, C=0, L=0, R=0)
	# ...by taking the touch pad values...
	tAv = tA.raw_value
	tBv = tB.raw_value
	tCv = tC.raw_value
	# ...and saving the state if it's greater than the minimum touch value...
	st["A"] = tAv >= tAl[0]
	st["B"] = tBv >= tBl[0]
	st["C"] = (tCv >= tCl)
	# ...and record if the L and R physical buttons are active too.
	st["L"]  = bL.value
	st["R"]  = bR.value
	
	# A shortcut to see if *any* button is down, take the sum of the values.
	# The values in the dictionary will be 0 if False and 1 if True
	bDwn = sum(st.values())
	if not bDwn:
		# The sum was zero, no buttons are being held down.
		# Call the callback to release any keys, just to make sure that all keys are up
		cbackRelease()
		# Keys are no longer active...
		kActv = False
		# ...and the highest readings from touch A and touch B can be reset.
		tAh = 0
		tBh = 0
	# If the button state is different than the previous button state (something happened!)
	if not st == prev:
		# Replace the previous state wieh the current state and reset the timer.
		# The timer is important because we don't want to take action on these newbutton changes yet --
		# we need to wait and make sure that the buttons are finished being pressed.
		prev.update(st)
		prevT = time.monotonic()
	# Now, if the buttons are still down,
	# and the state hasn't changed,
	# and the timer has exceeded the "dly" time of 1/20th of a second:
	if bDwn and (time.monotonic() - prevT > dly):
		# If no keys are currently active
		# (block the change of keystrokes if you're holding a key and slip and touch another one)
		if not kActv:
			kActv = True
			# Decide on how to take action.
			# If the "middle" button is touched, only the "C" pad state will have changed but not "A" or "B".
			# If the "C" pad along with "A" or "B" changed, then the "Up" or "Down" buttons were pressed
			# (Remember, those Up and Down pads are really touch touch pads in one!)
			if st["C"]:
				if not 1 in [st["A"], st["B"]]: cMID()
				elif st["A"]: cDOWN()
				elif st["B"]: cUP()
			# Ot, the "C" pad wasn't touched, but the "A" or "B" were touched on their own.
			# In this case, don't send the *current* touch value, send the *highest* touch value that these
			# touch pads recorded over the last 1/20th of a second. It might only currently be a very tiny touch,
			# but a small moment ago it may have been a very firm touch.
			elif st["A"] and not st["B"]: cA(tAh)
			elif st["B"] and not st["A"]: cB(tBh)
			# If the "L" and "R" buttons were pressed at the same time, recalibrate the touch sensors!
			if st["L"] and st["R"]:
				minA, minB, minC = calibrate()
			# Otherwise, hit the callback for the "L" or "R" on their own.
			elif st["L"]: cL()
			elif st["R"]: cR()
	elif bDwn:
		# If the buttons are down, but if the timer hasn't exceeded the 1/20th of a second yet,
		# continue to record the highest value that occurs on the "A" and "B" touch pads
		if tAv > tAh: tAh = tAv
		if tBv > tBh: tBh = tBv
		
""" And that's it! """
