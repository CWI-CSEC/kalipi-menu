#!/usr/bin/env python

#Headers
import RPi.GPIO as GPIO
import time
import subprocess
import uinput

#House keeping for GPIO
GPIO.setmode(GPIO.BCM)

#Declaring buttons
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #CIRCLE
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #SQUARE
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #TRIANGLE
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #X
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #DOWN
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #UP
GPIO.setup(27, GPIO.OUT)			  #Backlight

#To declare keys to emulate using uinput
device = uinput.Device([
        uinput.KEY_UP,
        uinput.KEY_DOWN,
	uinput.KEY_TAB,
	uinput.KEY_ENTER,
	uinput.KEY_LEFTCTRL,
	uinput.KEY_C
        ])
device.emit_combo([
        uinput.KEY_LEFTCTRL,
        uinput.KEY_C,
        ])

GPIO.output(27,GPIO.HIGH) #Start the backlight as ON

def main():
	#Start loop to check button status
	while True:
    		input_state23 = GPIO.input(23)
    		input_state22 = GPIO.input(22)
    		input_state24 = GPIO.input(24)
    		input_state5 = GPIO.input(5)
    		input_state17 = GPIO.input(17)
    		input_state4 = GPIO.input(4)
		#CIRCLE
    		if input_state23 == False and input_state4 == True and input_state17 == True:
			#subprocess.call(['lxterm', '-T', 'Test', '-e', 'ls;bash'])
			time.sleep(0.4)
		#SQUARE
    		if input_state22 == False and input_state4 == True and input_state17 == True:
        		time.sleep(0.4)
		#TRIANGLE (Tab)
    		if input_state24 == False and input_state4 == True and input_state17 == True:
			device.emit_click(uinput.KEY_TAB)
        		time.sleep(0.4)
		#X (Enter)
    		if input_state5 == False and input_state4 == True and input_state17 == True:
			device.emit_click(uinput.KEY_ENTER)
        		time.sleep(0.4)
		#UP (Up arrow)
    		if input_state17 == False and input_state23 == True and input_state22 == True and input_state24 == True and input_state5 == True:
			device.emit_click(uinput.KEY_UP)
        		time.sleep(0.2)
		#DOWN (Down arrow)
    		if input_state4 == False and input_state23 == True and input_state22 == True and input_state24 == True and input_state5 == True:
			device.emit_click(uinput.KEY_DOWN)
        		time.sleep(0.2)
		#CIRCLE and UP (reboot)
    		if input_state23 == False and input_state17 == False:
        		time.sleep(1)
        		subprocess.call(['reboot'])
		#CIRCLE and DOWN (shutdown)
    		if input_state23 == False and input_state4 == False:
        		time.sleep(1)
			subprocess.call(['shutdown', '-h', 'now'])
		#SQUARE and UP (Backlight On)
    		if input_state22 == False and input_state17 == False:
			GPIO.output(27,GPIO.HIGH)
			time.sleep(0.2)
		#SQUARE and DOWN (Backlight Off)
    		if input_state22 == False and input_state4 == False:
        		GPIO.output(27,GPIO.LOW)
        		time.sleep(0.2)
		#TRIANGLE and UP (CTRL-C)
    		if input_state24 == False and input_state17 == False:
        		#device.emit_combo(uinput.KEY_LEFTCTRL)
        		#device.emit_combo(uinput.KEY_C)
        		time.sleep(0.2)
		#TRIANGLE and DOWN (Brief Ifconfig)
    		if input_state24 == False and input_state4 == False:
        		subprocess.call(['lxterm', '-T', 'IP ADDRESS', '-e',"ifconfig | grep 'inet ' | awk '{print $2, $4}';bash"])
        		time.sleep(0.2)
    		time.sleep(0.1)
		#X and UP (Start the GUI, STARTX)
    		if input_state5 == False and input_state17 == False:
			subprocess.call(['lxterm','-T','MENU','-e','sudo startx'])
		#X and DOWN (OPEN MENU) WIP
    		if input_state5 == False and input_state4 == False:
			subprocess.call(['lxterm','-T','MENU','-e','sudo python ~/bin/menu.py;bash'])
    		time.sleep(0.1)
	main()

#MAKES SURE ALL FUNCTIONS ARE DECLARED AND RETURNS TO THE TOP
if __name__ == '__main__':
    main()