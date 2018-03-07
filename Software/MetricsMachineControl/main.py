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

# Touch sensitivity levels
lvls = [0.07, 0.31, 0.43]

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
	# Unassigned
	print("Mid")
	dot[0] = (64, 64, 0)

def cL():
	# Show Glyph Stack
	k.press(Keycode.GUI, Keycode.G)
	print("L")
	led.value = 1
	# cmd-E

def cR():
	# Flip Pair
	k.press(Keycode.GUI, Keycode.F)
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

def calibrate():
	sTime = time.monotonic()
	rA = [4094, 0]
	rB = [4094, 0]
	rC = [4094, 0]
	t = 4
	while sTime+t>=time.monotonic():
		led.value = 1
		if time.monotonic()-sTime>1:
			f = time.monotonic()%0.1 > 0.05
			led.value = not f
			dot[0] = (f*255,0,0)
			vA = tA.raw_value
			if vA<rA[0]: rA[0]=vA
			elif vA>rA[1]: rA[1]=vA
			vB = tB.raw_value
			if vB<rB[0]: rB[0]=vB
			elif vB>rB[1]: rB[1]=vB
			vC = tC.raw_value
			if vC<rC[0]: rC[0]=vC
			elif vC>rC[1]: rC[1]=vC
	mA = rA[0]+(rA[1]-rA[0])*6
	mB = rB[0]+(rB[1]-rB[0])*6
	mC = rC[0]+(rC[1]-rC[0])*6
	led.value = 0
	dot[0] = (0,255,0)
	time.sleep(0.25)
	dot[0] = (0,0,0)
	print(mA,mB,mC)
	return mA,mB,mC
minA, minB, minC = calibrate()

def vl(m, *l):
	return [m+((4096-m)*i) for i in l]
tAl = vl(minA, *lvls)
tBl = vl(minB, *lvls)
tCl = vl(minC, 0.4)[0]

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
			if st["L"] and st["R"]:
				minA, minB, minC = calibrate()
			elif st["L"]: cL()
			elif st["R"]: cR()
	elif bDwn:
		if tAv > tAh: tAh = tAv
		if tBv > tBh: tBh = tBv
