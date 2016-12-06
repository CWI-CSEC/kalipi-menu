#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os
import subprocess
import uinput


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #UP
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #DOWN
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #X, which is enter
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Triangle
GPIO.setup(27, GPIO.OUT)			  #Backlight



keys = (uinput.KEY_LEFTCTRL, uinput.KEY_LEFTALT, uinput.KEY_F1, uinput.KEY_N, uinput.KEY_ENTER)
device = uinput.Device(keys)


def main():
    option = 1 #Declare option variable

#    os.system('clear')
    menu()
#    print "Choose: "
    checker(option)
    option = optionCHK
    selection(option)
    print "%d. %s" %(option,show)
    input_state5 = GPIO.input(5)
    #none = raw_input("Choose one: ")
    GPIO.output(27,GPIO.HIGH) #Start the backlight
    while input_state5 == True:
	input_state17 = GPIO.input(17)
	input_state4 = GPIO.input(4)
	input_state5 = GPIO.input(5)

	if input_state4 == False: #If DOWN pressed
	    option += 1
	    checker(option) #Check if its over/under
	    option = optionCHK #Reset option in case it was over/under
	    menu() #Reprint menu
	    selection(option) #Show the user what they're selecting
	    print "%d. %s" %(option,show)
	if input_state17 == False: #If UP pressed
	    option -= 1
	    checker(option) #Check if its over/under
	    option = optionCHK #Reset option in case it was over/under
	    menu() #Reprint menu
            selection(option) #Show the user what they're selecting
            print "%d. %s" %(option,show)
	time.sleep(0.25)
    display(option) #Display whatever was asked for
    main() #Returns to the menu when they're done

#FOR DISPLAYING THE REQUESTED INFORMATION
def display(option):
    if option == 0:
        main()
    if option == 1:
        #For ifconfig code
	global INT
	INT = 'br0'
	testint(INT)
	INT = 'eth0'
	testint(INT)
	INT = 'wlan0'
	testint(INT)
	INT = 'wlan1'
	testint(INT)
	INT = 'wlan2'
	testint(INT)
	INT = 'wlan3'
	testint(INT)
	INT = 'wlan4'
	testint(INT)
	print "---PRESS X TO RETURN---"
        time.sleep(0.5)
        input_state5 = GPIO.input(5)
        while input_state5 == True:
                input_state5 = GPIO.input(5)
                time.sleep(0.2)
    if option == 2:
	#Turn screen on
	GPIO.output(27,GPIO.HIGH)
	main()
    if option == 3:
	#Turn screen off
	GPIO.output(27,GPIO.LOW)
	main()
    if option == 4:
	#PLACEHOLDER FOR HOTSPOT CODE
	print "Are you sure you want to convert WLAN1 to a hotspot?"
	print "X: YES"
	print "Triangle: NO"
	time.sleep(0.5)
        input_state5 = GPIO.input(5)
	input_state24 = GPIO.input(24)
        while input_state5 == True and input_state24 == True:
                input_state5 = GPIO.input(5)
		input_state24 = GPIO.input(24)
                time.sleep(0.2)
	if input_state24 == False:
		main()
	if input_state5 == False:
		os.popen('cp /etc/hostapd/HOThostapd.conf /etc/hostapd/hostapd.conf').read().strip()
		os.popen('cp /etc/network/HOTinterfaces /etc/network/interfaces').read().strip()
		os.popen('systemctl start hostapd').read().strip()
		os.popen('systemctl start dnsmasq').read().strip()
	print "Would you like to enable this mode at startup?"
	print "X: YES"
        print "Triangle: NO"
        time.sleep(0.5)
        input_state5 = GPIO.input(5)
        input_state24 = GPIO.input(24)
        while input_state5 == True and input_state24 == True:
                input_state5 = GPIO.input(5)
                input_state24 = GPIO.input(24)
                time.sleep(0.2)
        if input_state24 == False:
                main()
        if input_state5 == False:
		print "Enabling..."
		os.popen('systemctl enable hostapd').read().strip()
                os.popen('systemctl enable dnsmasq').read().strip()
		time.sleep(0.5)
    if option == 5:
	#Disable GUI
	print "Disabling GUI"
	os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4.1.21-20160822/re4son-pi-tft-setup -b cli").read().strip()
        print "X: Later"
        print "TRIANGLE: Reboot"
	input_state5 = GPIO.input(5)
	input_state24 = GPIO.input(24)
	while input_state5 == True and input_state24 == True:
	    input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
	    time.sleep(0.2)
	if input_state24 == False:
	    print "Rebooting..."
	    time.sleep(1)
	    subprocess.call(['reboot'])
	if input_state5 == False:
	    print "Returning to menu..."
	    time.sleep(1)
    if option == 6:
	#Enable GUI
	print "Enabling GUI"
        os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4.1.21-20160822/re4son-pi-tft-setup -b gui").read().strip()
        print "X: Later"
        print "TRIANGLE: Reboot"
        input_state5 = GPIO.input(5)
        input_state24 = GPIO.input(24)
        while input_state5 == True and input_state24 == True:
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            time.sleep(0.2)
        if input_state24 == False:
            print "Rebooting..."
            time.sleep(1)
            subprocess.call(['reboot'])
        if input_state5 == False:
            print "Returning to menu..."
            time.sleep(1)
    if option == 7:
	#Enable Auto-login
	print "Enabling auto-login"
        os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4.1.21-20160822/re4son-pi-tft-setup -a root").read().strip()
    if option == 8:
	#Disable Auto-login
        print "Disabling auto-login"
        os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4.1.21-20160822/re4son-pi-tft-setup -a disable").read().strip()
    if option == 9:
	#Wifi Menu
	subprocess.call(['nmtui'])
    if option == 10:
	#Bluetooth Menu
	subprocess.call(['bluetoothctl'])
    if option == 11:
	#Enable NORMAL Wifi mode
	print "Please wait..."
	os.popen('cp /etc/network/NORMinterfaces /etc/network/interfaces').read().strip()
	print "Triangle: Enable Now"
	print "X: Enable at reboot"
	input_state5 = GPIO.input(5)   #X
        input_state24 = GPIO.input(24) #Triangle
        while input_state5 == True and input_state24 == True:
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            time.sleep(0.2)
        if input_state24 == False:
            print "Enabling now..."
	    os.popen('systemctl stop dnsmasq').read().strip()
	    os.popen('systemctl stop hostapd').read().strip()
            os.popen('systemctl restart networking').read().strip()
	    os.popen('iwconfig wlan0 mode managed').read().strip()
	    os.popen('iwconfig wlan0 power on').read().strip()
        if input_state5 == False:
            print "Enabling next reboot"
            time.sleep(3)
    if option == 12:
	#Enable BRIDGED ADAPTOR
	print "Please wait..."
	os.popen('cp /etc/hostapd/BRIhostapd.conf /etc/hostapd/hostapd.conf').read().strip()
	os.popen('cp /etc/network/BRIinterfaces /etc/network/interfaces').read().strip()
	print "Connect using:"
	INT = 'br0'
	testint(INT)
	print "Triangle: Enable Now"
        print "X: Enable at reboot"
        input_state5 = GPIO.input(5)   #X
        input_state24 = GPIO.input(24) #Triangle
        while input_state5 == True and input_state24 == True:
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            time.sleep(0.2)
        if input_state24 == False:
            print "Enabling now..."
            os.popen('systemctl restart networking').read().strip()
	    os.popen('systemctl start hostapd').read().strip()
	if input_state5 == False:
            print "Enabling next reboot"
            time.sleep(3)
    if option == 13:
	#Disable Tunneling
	os.popen('cp /etc/ssh/NORMsshd_config /etc/ssh/sshd_config').read().strip()
	os.popen('cp /lib/systemd/system/NORMssh.socket /lib/systemd/system/ssh.socket').read().strip()
	os.popen('systemctl daemon-reload').read().strip()
	os.popen('systemctl restart ssh.socket').read().strip()
    if option == 14:
	#Enable Tunneling
	os.popen('cp /etc/ssh/TUNsshd_config /etc/ssh/sshd_config').read().strip()
        os.popen('cp /lib/systemd/system/TUNssh.socket /lib/systemd/system/ssh.socket').read().strip()
	os.popen('systemctl daemon-reload').read().strip()
        os.popen('systemctl restart ssh.socket').read().strip()
	print "Tunnel home [X] or other [TRIANGLE]"
	print "Note: Other requires keyboard"
	input_state5 = GPIO.input(5)   #X
        input_state24 = GPIO.input(24) #Triangle
        while input_state5 == True and input_state24 == True:
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            time.sleep(0.2)
	if input_state5 == False: #X
            os.popen('clear').read().strip()
            print "Use this to connect: ssh -X -l root -p 5555 localhost"
            print "---Press X to start---"
	    time.sleep(0.5)
            input_state5 = GPIO.input(5)
	    while input_state5 == True:
                input_state5 = GPIO.input(5)
                time.sleep(0.2)
	    print "Tunneling..."
            #Declaring variables for a home base machine.
            homeuser = "changeme"
            homeip = "changeme"
            homeport = "changeme"
            print "Command returns: %s" %os.popen('ssh -N -R 5555:localhost:32395 %s@%s -p %s'%(homeuser,homeip,homeport)).read().strip()
            print "---Press X for menu---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            while input_state5 == True:
                input_state5 = GPIO.input(5)
                time.sleep(0.2)
        if input_state24 == False: #Triangle
	    user = raw_input("Username: ")
	    ip = raw_input("External IP: ")
	    port = raw_input("External Port:  ")
	    os.popen('clear').read().strip()
	    print "Use this to connect: ssh -X -l root -p 5555 localhost"
            print "---Press X to start---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            while input_state5 == True:
                input_state5 = GPIO.input(5)
                time.sleep(0.2)
	    print "Tunneling..."
	    print "Command returns: %s" %os.popen('ssh -N -R 5555:localhost:32395 %s@%s -p %s'%(user,ip,port)).read().strip()
	    print "---Press X for menu---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            while input_state5 == True:
                input_state5 = GPIO.input(5)
                time.sleep(0.2)
    if option == 15:
	print "Restarting..."
	time.sleep(2)
	os.popen('reboot').read().strip()
    if option == 16:
	print "Shutting Down..."
	time.sleep(2)
	os.popen('shutdown -h now').read().strip()
    if option == MAX:
	print "GOODBYE"
	exit()

#FOR RETURNING WHAT OPTION THEY CURRENTLY HAVE SELECTED
def selection(option):

    global show
    if option == 1:
	show = "Ifconfig"
    if option == 2:
	show = "Screen On"
    if option == 3:
	show = "Screen Off"
    if option == 4:
	show = "Hotspot"
    if option == 5:
	show = "Disable GUI"
    if option == 6:
	show = "Enable GUI"
    if option == 7:
	show = "Enable Auto Login"
    if option == 8:
	show = "Disable Auto Login"
    if option == 9:
	show = "Wifi Menu"
    if option == 10:
	show = "Bluetooth Menu"
    if option == 11:
	show = "Network Defaults"
    if option == 12:
	show = "Bridge Eth0 + Wlan0"
    if option == 13:
	show = "Disable SSH Tunnel"
    if option == 14:
	show = "Enable SSH Tunnel"
    if option == 15:
	show = "Reboot"
    if option == 16:
	show = "Shutdown"
    if option == MAX:
	show = "EXIT"
    return show;

#FOR REPRINTING THE MENU
def menu():
    os.system('clear')
    print "---------"
    print "|  MENU  |"
    print "---------"
#    print "Choose: "
    return 0

#CHECKS IF THE OPTION IS WAY OVER OR UNDER THE LIMIT
def checker(option):
    global optionCHK
    optionCHK = option
    MIN = 1
    global MAX
    MAX = 17
    if (option < MIN):
	optionCHK = MIN
    if (option > MAX):
	optionCHK = MAX
    return optionCHK

#FOR TESTING INTERFACES
def testint(INT):
    SEARCH = "grep %s /proc/net/dev" %INT
    ISUP = os.popen(SEARCH).read().strip()
    if not ISUP == "":
	IP = os.popen('ip addr show %s | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''%INT).read().strip()
	print "%s: %s" %(INT,IP)
    return 0



#MAKES SURE ALL FUNCTIONS ARE DECLARED AND RETURNS TO THE TOP
if __name__ == '__main__':
    main()
