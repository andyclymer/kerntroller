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

## The Hardware

The KernTroller hardware was designed with the hope that it's easy to build, and consists of one custom PCB, the Adafruit Trinket M0 dev board, and a couple of buttons. An overview of the hardware and a build guide can be found in the [Hardware](/Hardware) directory of this repo.


## The Software

The best part — it's easy to customize how the KernTroller functions by editing a few lines of Python code! The Trinket M0 simply mounts as a drive on your computer, giving you direct access to the code living within. Sample presets and an overview of how the software works can be found in the [Software](/Software) directory of this repo.

## Let me know what you think!

Let me know if you have any questions, or if you made one yourself! I'm also available to give a small workshop on an introduction to electronics and Python by building and programming the KernTroller, [so get in touch!](http://www.andyclymer.com/)


