# kalipi-menu
A menu system for use with Kali Linux on the Raspberry Pi with a TFT case and physical buttons.

Created for use with the [Uniker RS-002 6-button case](https://www.amazon.com/Uniker-Raspberry-Aluminum-Enclosure-Screen/dp/B014JFEU48/), and alongside [Re4son's Kali Linux guide](http://whitedome.com.au/re4son/sticky-fingers-kali-pi/).



For the menu script, use the arrow keys (keyboard or on the case) to navigate up and down the menu. The X button (or right arrow on keyboard) selects the current option and any further functions of the buttons are displayed on the screen.

For the button scripts, the "button.py" file checks if you're running in CLI or GUI mode and then executes the correct script. These can be customized. 




To install:

`cd ~`

`mkdir bin`

`cd bin`

`git clone https://github.com/kforney/kalipi-menu`

`cd kalipi-menu/bin`

`chmod +x install`

`./install`
