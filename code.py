# Pico Blender Doorbell
# Rob_on_Earth 2021
import time
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


# move the mouse by maximum jumps with delays 
def move_mouse_by(x, y, mouse, delay, jump):
    print("MMB({0}, {1})".format(x, y))
    while (x != 0 or y != 0):
        mx = limit(x, jump)
        my = limit(y, jump)
        mouse.move(mx, my)
        x -= mx
        y -= my
        time.sleep(delay)
    
    
# limit a number to plus and minus "by"
def limit(value, by):
    return min(by, max(-by, value))


# Moves the mouse to the top left and then the center of the screen
# requires screen to be correctly defined
# delay and jump parameters are to allow for mouse acceleration on the target
def center_mouse(screen, mouse):
    move_mouse_by(-screen["width"], -screen["height"], mouse, 0, 100)
    move_mouse_by(int(screen["width"] /2), int(screen["height"] /2), mouse, 0.02, 5)
    

# loops infinitely waiting for a button press
def button_loop(led, btn, keystrokes, keyboard, mouse, screen):
    while True:
        led.value = True
        if btn.value:
            print("Btn pressed")
            led.value = False
            do_blender_save_as(keystrokes, keyboard, screen, mouse)
            time.sleep(10)
        time.sleep(0.1)


# Send keystrokes with delay to keyboard interface
def send_keystrokes(keystrokes, keyboard, delay):
    for keystroke in keystrokes:
        if type(keystroke) is list:
            keyboard.send(*keystroke)
        else:
            keyboard.send(keystroke)
        time.sleep(delay)
    
    
# Center the mouse and then send keystrokes        
def do_blender_save_as(keystrokes, keyboard, screen, mouse):
    center_mouse(screen, mouse)
    send_keystrokes(keystrokes, keyboard, 1)
   
   
def main():
    # Set up a input button on GPIO Pin 15
    btn_pin = board.GP15
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN

    # Set up the Pico onboard LED 
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    
    # Create Mouse and Keybord devices
    mouse = Mouse(usb_hid.devices)
    keyboard = Keyboard(usb_hid.devices)
    # List the keystrokes we want to initiate on button press
    keystrokes = [[Keycode.CONTROL, Keycode.SHIFT, Keycode.S], Keycode.KEYPAD_PLUS, Keycode.ENTER]
    # define the target screen size
    screen = {"width":1920, "height":1080}
    button_loop(led, btn, keystrokes, keyboard, mouse, screen)
    
    
main()
