# kalipi-menu
A menu system for use with Kali Linux on the Raspberry Pi with a TFT case and physical buttons.

Created for use with the [Uniker RS-002 6-button case](https://www.amazon.com/Uniker-Raspberry-Aluminum-Enclosure-Screen/dp/B014JFEU48/), and alongside [Re4son's Sticky Fingers Kali guide](http://whitedome.com.au/re4son/sticky-fingers-kali-pi/).

# Usage

Run "buttons.py".  It should check if you're running in CLI or GUI mode and then execute the correct script.

Use the arrow keys (keyboard or on the case) to navigate up and down the menu. The X button (or right arrow on keyboard) selects the current option and any further functions of the buttons are displayed on the screen.

The menu itself can be found in "menu.py", and customized to your liking.


# Installation:

`git clone https://github.com/CWI-ISDF/kalipi-menu`

`cd kalipi-menu`

`./install.sh`
