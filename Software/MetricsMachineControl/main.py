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

Read the fully commented version here:
https://github.com/andyclymer/kerntroller
"""

# Calibration Data
# Replace with actual values from the "Calibrate" script
minA = 1507
minB = 1845
minC = 3219

# Touch sensitivity levels
lvls = [0.04, 0.25, 0.4]

# LED brightness (0-1)
lB = 0.05


# Callbacks

def cUP():
	# Previous Pair
	print("Up")
	k.press(Keycode.UP_ARROW)
	dot[0] = (0, 0, 255)

def cDOWN():
	# Next Pair
	print("Down")
	k.press(Keycode.DOWN_ARROW)
	dot[0] = (0, 0, 255)

def cA(v):
	# Negative Kern
	l = sum([v>=i for i in tAl])
	print("A", l)
	if l == 1: k.press(Keycode.ALT, Keycode.LEFT_ARROW)
	elif l == 2: k.press(Keycode.SHIFT, Keycode.LEFT_ARROW)
	elif l == 3: k.press(Keycode.LEFT_ARROW)
	dot[0] = (85*l, (l>2)*128, (l>1)*128)
	
def cB(v):
	# Positive Kern
	l = sum([v>=i for i in tBl])
	print("B", l)
	if l == 1: k.press(Keycode.ALT, Keycode.RIGHT_ARROW)
	elif l == 2: k.press(Keycode.SHIFT, Keycode.RIGHT_ARROW)
	elif l == 3: k.press(Keycode.RIGHT_ARROW)
	dot[0] = ((l>2)*128, 85*l, (l>1)*128)

def cMID():
	# Flip Pair
	k.press(Keycode.GUI, Keycode.F)
	print("Mid")
	dot[0] = (64, 64, 0)

def cL():
	# Break Exception
	k.press(Keycode.GUI, Keycode.ALT, Keycode.E)
	print("L")
	led.value = 1
	# cmd-E

def cR():
	# Make Exception
	k.press(Keycode.GUI, Keycode.E)
	print("R")
	led.value = 1
	
def cbackRelease():
	k.release_all()
	dot[0] = (0, 0, 0)
	led.value = 0



dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=lB)
dot[0] = (0, 0, 0)

k = Keyboard()
kL = KeyboardLayoutUS(k)

bR = DigitalInOut(board.D2)
bR.direction = Direction.INPUT
bR.pull = Pull.DOWN

bL = DigitalInOut(board.D0)
bL.direction = Direction.INPUT
bL.pull = Pull.DOWN

tA = touchio.TouchIn(board.D3)
tB = touchio.TouchIn(board.D4)
tC = touchio.TouchIn(board.D1)

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

def vl(m, *l):
	return [m+((4096-m)*i) for i in l]
tAl = vl(minA, *lvls)
tBl = vl(minB, *lvls)
tCl = vl(minC, 0.3)[0]


prev = dict(A=0, B=0, C=0, L=0, R=0)
prevT = time.monotonic()
dly = 0.05
kActv = False
tAh = 0
tBh = 0

while True:
	
	st = dict(A=0, B=0, C=0, L=0, R=0)
	tAv = tA.raw_value
	tBv = tB.raw_value
	tCv = tC.raw_value
	
	st["A"] = tAv >= tAl[0]
	st["B"] = tBv >= tBl[0]
	st["C"] = (tCv >= tCl)
	
	st["L"]  = bL.value
	st["R"]  = bR.value
	
	bDwn = sum(st.values())
	if not bDwn:
		cbackRelease()
		kActv = False
		tAh = 0
		tBh = 0
	if not st == prev:
		prev.update(st)
		prevT = time.monotonic()
	if bDwn and (time.monotonic() - prevT > dly):
		if not kActv:
			kActv = True
			if st["C"]:
				if not 1 in [st["A"], st["B"]]: cMID()
				elif st["A"]: cDOWN()
				elif st["B"]: cUP()
			elif st["A"] and not st["B"]: cA(tAh)
			elif st["B"] and not st["A"]: cB(tBh)
			elif st["L"]: cL()
			elif st["R"]: cR()
	elif bDwn:
		if tAv > tAh: tAh = tAv
		if tBv > tBh: tBh = tBv
