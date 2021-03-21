Pico Blender Doorbell

Install:
Raspberry Pi Pico with Circuit Python (tested with version 6.2.0-beta.3 on 2021-03-04)
https://circuitpython.org/board/raspberry_pi_pico/

Add Adafruit HID library
https://github.com/adafruit/Adafruit_CircuitPython_HID
(extract it to the Pico's lib folder

copy code.py to the root of the Pi.


Usage:
Plug into your target computer with USB cable and when the green power LED is lit on your Pico press the button.


Notes:
Currently hardwired to 1920x1080 screen resolution, but should work reasonbly on other resolutions.
Feel free to change the hardcoded value in code.py file to fit your needs.

There is a delibarate delay after pressing the button before new presses will be recognised. Only when the LED is lit is the device ready to accept another press.
