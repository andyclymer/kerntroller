# KernTroller Hardware

![Kerntroller Front](/images/kerntroller-osh-front.png)

![Kerntroller Back](/images/kerntroller-osh-back.png)

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



