# KernTroller

![Kerntroller Front](/images/KernTroller-Front.jpg)

![Kerntroller Back](/images/KernTroller-Back.jpg)

The **KernTroller** is a customizable keyboard controller with pressure sensitive capacitive touch pads, based on the [Adafruit Trinket M0](https://www.adafruit.com/product/3500) board, and is programmable with [CircuitPython](https://circuitpython.readthedocs.io/en/2.x/)!

The default configuation has you ready to kern in [Type Supply MetricsMachine](http://tools.typesupply.com/) but its functionality is easy to customize by changing a few lines of Python code. Essentially, your computer sees it as a keyboard, and the mapping of button presses to keyboard keystrokes is all outlined in a Python script running on the device!

The capacitive touch pads can sense a range of values depending on how firmly you press down on the “button”, and can then trigger different keyboard shortcuts accordingly.

The KernTroller was also designed to use a minimal set of components, making it relatively easy to build.

![Default button setup](/images/MMLayout.gif)


## What's this?

Back at [RoboThon 2015](https://vimeo.com/album/3329572) I presented some of my thoughts and experiments with making custom controllers for type design, and at that time CJ Dunn observed that MetricsMachine looks like it's practically designed to be used with a video game controller. [USB video game controllers can be found relatively cheaply](https://www.google.com/search?q=usb+super+nintendo+controller), and it turns out to actually be a really nice way to interact with a repetitive task that only needs 6 keys to perform.

I learned more about building things in the mean time, and three years later, at RoboThon 2018, I better have something to show for it!

## Why make one when you can just buy a cheap controller?

Now *you’re* trolling *me!*

![Kerntroller PCB](/images/KernTroller-PCB.jpg)

# Hardware

## Components
- One *KernTroller PCB*
- One *Adafruit Trinket M0*
- Two *five-pin 0.1in (2.45mm) spaced header strips* (included with the Trinket M0)
- Two *6mm “tactile buttons”*
- One *USB Micro-B cable*
- Optional: *Little plastic widget* to keep you from touching the pins on the back of the device

## Where to buy
- **KernTroller PCBs:** I'm currently checking for interest on a cheaper second run of PCBs, so let me know if you would like to build one! In the mean time, KernTroller PCBs can be purchased in shareable packs of three [directly from the PCB manufacturer OSH Park](https://oshpark.com/shared_projects/DCge5Fbd) at a cost of $19.95 for the set
- **Adafruit Trinket M0:** In the United States, the Trinket M0 can be [purchased from Adafruit](https://www.adafruit.com/product/3500) for about $9 each or for a little bit more [on Amazon](https://www.amazon.com/Adafruit-Trinket-M0-CircuitPython-Arduino/dp/B01MR2S7K0/). Just be absolutely sure to purchase the black “Trinket M0” and not the blue “Trinket 5V” or “Trinket 3.3V”!
- **6mm Tactile Buttons:** These are very common parts, [a bag can be purchased from Adafruit](https://www.adafruit.com/product/367) or from [Tayda Electronics](https://www.taydaelectronics.com/tact-switch-6x6mm-4-3mm-through-hole-spst-no.html) (4c each, can't beat it!)
- I've laser cut several **little plastic widgets** that can be attached to the back of the controller to keep your hands from touching the pin connectons on the back — an accidental touch could be read as a button press. Contatct me and I'll put one in the mail, or feel free to laser cut or 3D print your own from the files in the GitHub repo.

## How to build

### Required tools:

- Soldering iron
- Solder
- Clipper tool (AKA “sprue cutters”, “flush cutters”, or “right angle clippers”)
- Isoproply alcohol for cleaning

Collect your components (listed above).

If you purchased PCBs directly from OSH Park, they will likely have small tabs around the edges which are meant to break away. The prototyping service manufactures PCBs ganged up in larger boards with other projects, so you might want to snap these off first and even sand down the edges just a bit.

The Adafruit Trinket M0 should come with one long strip of pin headers, start by breaking it apart to yield the two required five-pin sections.

Fit the pin headers between the KernTroller PCB and the Trinket M0. Solder one header pin to the Trinket M0 and confirm that everything still sits squarely before continue to solder the reamining pins to the Trinket M0. Then, flip everything over and solder the header pins to the Kern>Troller PCB.

Clip the excess length of the pins as closely as you can to the Trinket M0 and Kern>Troller PCB.

Fit the two 6mm tactle buttons. They should only fit in an orientation where their legs are pointed toward the top and bottom of the KernTroller PCB. Turn the PCB over and solder them to attach, and then clip the remaining lenght of their legs as closely to the PCB as possible.

After clipping all of the pins, it might be nice to touch the soldering iron briefly to each solder joint to make it a bit smoother.

*Important step:* Clean off all of your solder joints with isopropyl alcohol (“rubbing alcohol”) even if you were using "no-clean solder" — the residue is still toxic and should be cleaned off since the circuit board isn't going to live within an enclosure. Don't skip this step!

Finally, if you have the “small laser cut plastic widget”, affix it to the back of the board to cover the touch contacts. If you aren't able to obtain this piece, at least cover the contacts with a bit of electrical tape to keep them from shorting if they touch a metal surface.

## How it works

@@@ TK

# Software

When you connect the KernTroller (or rather the Adafruit Trinket M0) to your computer you'll find that it mounts as a small ``CIRCUITPY`` drive. It's set to run the ``main.py`` that it finds at the root level of its file system at startup, so all of your code editing will start with this file. I've included a few preset Python scripts that you can drop in and start using.

## How to install (and update CircuitPython)

@@@ TK

## How it works

@@@ TK

## How to modify

@@@ TK


