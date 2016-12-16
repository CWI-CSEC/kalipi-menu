#!/usr/bin/env python

# This file creates a menu meant to be navigated
# by the GPIO buttons on the Raspberry Pi case.
# The functions it performs sometimes rely on
# the script from Re4son. (https://whitedome.com.au/re4son/sticky-fingers-kali-pi/)
# User changeable variables are at the top of the
# file to make it easier.



import RPi.GPIO as GPIO
import time
import os
import subprocess
import re


GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #UP
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #DOWN
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #X, default "select" key
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Triangle
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #SQUARE
GPIO.setup(27, GPIO.OUT)			  #Backlight

abspath = os.path.abspath(__file__) #Makes the script find where its located so it can use relative paths
dname = os.path.dirname(abspath)
os.chdir(dname)

os.popen('chmod +x keytest').read().strip() #Set the permissions on the keyboard check file

global sshUSER
global sshIP
global sshPORT
global MAX

##############################################################################
# THESE VARIABLES CAN BE CUSTOMIZED FOR YOUR PURPOSES                        #
# YOU SHOULD EXCHANGE KEYS ON THE DEVICES SO                                 #
# YOU DON'T HAVE TO HAVE ANY KEYBOARD INPUT                                  #
# IF THIS IS AN EXTERNAL IP MAKE SURE PORT                                   #
# FORWARDING IS SET UP ON THE DESINATION ROUTER                              #
piPORT = "22"       #Port that you've opened on the Pi (Default:22)          #
sshUSER = "root"    #Username at destination (Default:root)                  #
sshIP = ""          #IP address of desination                                #
sshPORT = "22"      #Desination port (Default:22)                            #
#----------------------------------------------------------------------------#
#ONLY CHANGE THIS IF YOU ARE ADDING OR SUBTRACTING OPTIONS                   #
MAX = 17        #Number of options including "EXIT" (Default:17)             #
##############################################################################




def main():
    option = 1 #Declare option variable
    update(option)
    #TESTING CODE
    time.sleep(0.25)
    status = "backlight=1"
    if chkstatus(status) == 0:
        GPIO.output(27,GPIO.LOW)
    if chkstatus(status) == 1:
        GPIO.output(27,GPIO.HIGH)
    input_state5 = GPIO.input(5) #Check X key
    keyinput = os.popen("./keytest").read().strip() #Check arrow keys
    while input_state5 == True and keyinput != '2':             #Do this until the X button is pressed or KEY_RIGHT_ARROW
       input_state17 = GPIO.input(17)
       input_state4 = GPIO.input(4)
       input_state5 = GPIO.input(5)
       keyinput = os.popen("./keytest").read().strip() #Check arrow keys
       #Buttons are checked below
       if input_state17 == False or keyinput == '0': #If UP pressed or KEY_UP
          option -= 1
          option = update(option)
       if input_state4 == False or keyinput == '1': #If DOWN pressed or KEY_DOWN
          option += 1
          option = update(option)
       time.sleep(0.1)
    run(option) #Do whatever was selected
    main() #Returns to the menu when they're done





#FOR DISPLAYING THE REQUESTED INFORMATION
def run(option):
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
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and keyinput != '2':             #Do this until the X button is pressed or KEY_RIGHT_ARROW
            input_state5 = GPIO.input(5)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
    if option == 2:
    	#Turn screen on
    	GPIO.output(27,GPIO.HIGH)
        status = "bl=1"
        upstatus(status)
    	main()
    if option == 3:
    	#Turn screen off
    	GPIO.output(27,GPIO.LOW)
        status = "bl=0"
        upstatus(status)
    	main()
    if option == 4:
        #Disable GUI
        print "Disabling GUI"
        os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4*/re4son-pi-tft-setup -b cli").read().strip()
        print "X: Later"
        print "TRIANGLE: Reboot"
        input_state5 = GPIO.input(5)
        input_state24 = GPIO.input(24)
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
        if input_state24 == False or keyinput == '3':
            print "Rebooting..."
            time.sleep(1)
            subprocess.call(['reboot'])
        if input_state5 == False or keyinput == '2':
            print "Returning to menu..."
            time.sleep(1)
    if option == 5:
        #Enable GUI
        print "Enabling GUI"
        os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4*/re4son-pi-tft-setup -b gui").read().strip()
        print "X: Later"
        print "TRIANGLE: Reboot"
        input_state5 = GPIO.input(5)
        input_state24 = GPIO.input(24)
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
        if input_state24 == False or keyinput == '3':
            print "Rebooting..."
            time.sleep(1)
            subprocess.call(['reboot'])
        if input_state5 == False or keyinptu == '2':
            print "Returning to menu..."
            time.sleep(1)
    if option == 6:
       #Enable Auto-login
       print "Enabling auto-login"
       os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4*/re4son-pi-tft-setup -a root").read().strip()
    if option == 7:
       #Disable Auto-login
       print "Disabling auto-login"
       os.popen("echo 'N' | /usr/local/src/re4son_kali-pi-tft_kernel_4*/re4son-pi-tft-setup -a disable").read().strip()
    if option == 8:
	  #Wifi Menu
	  subprocess.call(['nmtui'])
    if option == 9:
	  #Bluetooth Menu
	  subprocess.call(['bluetoothctl'])
    if option == 10:
      #Enable NORMAL Wifi mode
      print "Please wait..."
      os.popen('cp /etc/network/NORMinterfaces /etc/network/interfaces').read().strip()
      print "Triangle: Enable Now"
      print "X: Enable at reboot"
      input_state5 = GPIO.input(5)   #X
      input_state24 = GPIO.input(24) #Triangle
      keyinput = os.popen("./keytest").read().strip() #Check arrow keys
      while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
          input_state5 = GPIO.input(5)
          input_state24 = GPIO.input(24)
          keyinput = os.popen("./keytest").read().strip() #Check arrow keys
          time.sleep(0.2)
      if input_state24 == False or keyinput == '3':
          print "Enabling now..."
          os.popen('systemctl stop dnsmasq').read().strip()
          os.popen('systemctl stop hostapd').read().strip()
          os.popen('systemctl restart networking').read().strip()
          os.popen('iwconfig wlan0 mode managed').read().strip()
          os.popen('iwconfig wlan0 power on').read().strip()
      if input_state5 == False or keyinput == '2':
          print "Enabling next reboot"
          time.sleep(3)
      status = "nw=NOR"
      upstatus(status)
    if option == 11:
    	#Enable BRIDGED ADAPTOR over WLAN0
        status = "network=NOR"
        if chkstatus(status) == 0: #If its not in normal mode
            os.popen('cp /etc/network/NORMinterfaces /etc/network/interfaces').read().strip()
            os.popen('systemctl stop dnsmasq').read().strip()
            os.popen('systemctl stop hostapd').read().strip()
            os.popen('systemctl restart networking').read().strip()
            os.popen('iwconfig wlan0 mode managed').read().strip()
            os.popen('iwconfig wlan0 power on').read().strip()
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
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
        if input_state24 == False or keyinput == '3':
            print "Enabling now..."
            os.popen('systemctl restart networking').read().strip()
    	    os.popen('systemctl start hostapd').read().strip()
    	if input_state5 == False or keyinput == '2':
            print "Enabling next reboot"
            time.sleep(3)
        status = "nw=BRI"
        upstatus(status)
    if option == 12:
        #Turns WLAN1 into a hotspot
    	print "Are you sure you want to convert WLAN1 to a hotspot?"
    	print "X: YES"
    	print "Triangle: NO"
    	time.sleep(0.5)
        input_state5 = GPIO.input(5)
    	input_state24 = GPIO.input(24)
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
    	if input_state24 == False or keyinput == '3':
    		main()
    	if input_state5 == False or keyinput == '2':
            status = "network=NOR"
            if chkstatus(status) == 0: #If its not in normal mode
                os.popen('cp /etc/network/NORMinterfaces /etc/network/interfaces').read().strip()
                os.popen('systemctl stop dnsmasq').read().strip()
                os.popen('systemctl stop hostapd').read().strip()
                os.popen('systemctl restart networking').read().strip()
                os.popen('iwconfig wlan0 mode managed').read().strip()
                os.popen('iwconfig wlan0 power on').read().strip()
	    print "Enabling..."
#	    os.popen('ifconfig wlan1 down').read().strip()
            os.popen('cp /etc/hostapd/HOThostapd.conf /etc/hostapd/hostapd.conf').read().strip()
       	    os.popen('cp /etc/network/HOTinterfaces /etc/network/interfaces').read().strip()
#	    os.popen('ifconfig wlan1 up').read().strip()
            os.popen('systemctl start hostapd').read().strip()
    	    os.popen('systemctl start dnsmasq').read().strip()
            print "Would you like to enable this mode at startup?"
       	    print "X: YES"
            print "Triangle: NO"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            while input_state5 == True and input_state24 == True and keyinput != '2' and keyinput != '3':
                input_state5 = GPIO.input(5)
                input_state24 = GPIO.input(24)
                keyinput = os.popen("./keytest").read().strip() #Check arrow keys
                time.sleep(0.2)
            if input_state24 == False or keyinput == '3':
                status = "nw=HOT"
                upstatus(status)
                main()
            if input_state5 == False or keyinput == '2':
           	print "Enabling..."
                os.popen('systemctl enable hostapd').read().strip()
                os.popen('systemctl enable dnsmasq').read().strip()
                status = "nw=HOT"
                upstatus(status)
   	    time.sleep(0.5)
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
    	print "Note: Both require keyboard"
    	print "(EXIT: SQUARE)"
    	input_state5 = GPIO.input(5)   #X
        input_state24 = GPIO.input(24) #Triangle
    	input_state22 = GPIO.input(22) #Square
        keyinput = os.popen("./keytest").read().strip() #Check arrow keys
        while input_state5 == True and input_state24 == True and input_state22 == True and keyinput != '2' and keyinput != '3':
            input_state5 = GPIO.input(5)
            input_state24 = GPIO.input(24)
    	    input_state22 = GPIO.input(22)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            time.sleep(0.2)
    	if input_state22 == False or keyinput == '3':
    		main()
    	if input_state5 == False or keyinput == '2': #X
            os.popen('clear').read().strip()
            print "Use this to connect: ssh -X -l root -p 5555 localhost"
            print "---Press X to start---"
    	    time.sleep(0.5)
            input_state5 = GPIO.input(5)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
    	    while input_state5 == True and keyinput != '2':
                    input_state5 = GPIO.input(5)
                    keyinput = os.popen("./keytest").read().strip() #Check arrow keys
                    time.sleep(0.2)
    	    print "Tunneling..."
            print "Command returns: %s" %os.popen('ssh -N -R 8888:localhost:%s %s@%s -p %s &' %(piPORT, sshUSER, sshIP, sshPORT)).read().strip()
            print "---Press X for menu---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            while input_state5 == True and keyinput != '2':
                input_state5 = GPIO.input(5)
                keyinput = os.popen("./keytest").read().strip() #Check arrow keys
                time.sleep(0.2)
        if input_state24 == False or keyinput == '3': #Triangle
    	    user = raw_input("Username: ")
    	    ip = raw_input("External IP: ")
    	    port = raw_input("External Port:  ")
    	    os.popen('clear').read().strip()
    	    print "Use this to connect: ssh -X -l root -p 5555 localhost"
            print "---Press X to start---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            while input_state5 == True and keyinput != '2':
                input_state5 = GPIO.input(5)
                keyinput = os.popen("./keytest").read().strip() #Check arrow keys
                time.sleep(0.2)
    	    print "Tunneling..."
    	    print "Command returns: %s" %os.popen('ssh -N -R 5555:localhost:%s %s@%s -p %s'%(piPORT, user,ip,port)).read().strip()
    	    print "---Press X for menu---"
            time.sleep(0.5)
            input_state5 = GPIO.input(5)
            keyinput = os.popen("./keytest").read().strip() #Check arrow keys
            while input_state5 == True and keyinput != '2':
                input_state5 = GPIO.input(5)
                keyinput = os.popen("./keytest").read().strip() #Check arrow keys
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
        show = "Disable GUI"
    if option == 5:
        show = "Enable GUI"
    if option == 6:
        show = "Enable Auto Login"
    if option == 7:
        show = "Disable Auto Login"
    if option == 8:
        show = "Wifi Menu"
    if option == 9:
        show = "Bluetooth Menu"
    if option == 10:
        show = "Network Defaults"
    if option == 11:
        show = "Bridge Eth0 + Wlan0"
    if option == 12:
        show = "Hotspot"
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
    return show

#FOR REPRINTING THE MENU
def menu():
    os.system('clear')
    print "*--------*"
    print "|  MENU  |"
    print "*--------*"
#    print "Choose: "
    return 0

#CHECKS IF THE OPTION IS WAY OVER OR UNDER THE LIMIT
def checker(option):
    optionCHK = option
    MIN = 1
    if (optionCHK < MIN):
    	optionCHK = MIN
    if (optionCHK > MAX):
    	optionCHK = MAX
    option = optionCHK
    return option

#FOR TESTING INTERFACES
def testint(INT):
    SEARCH = "grep %s /proc/net/dev" %INT
    ISUP = os.popen(SEARCH).read().strip()
    if not ISUP == "":
    	IP = os.popen('ip addr show %s | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''%INT).read().strip()
    	print "%s: %s" %(INT,IP)
    return 0

#UPDATES THE SCREEN WITH THE MENU AND CURRENT SELECTION
def update(option):
    # option = checker(option) #Reset option in case it was over/under limit
    menu() #Reprint menu
    # selection(option) #Find what option they're currently on
    print "%s. %s" %(checker(option),selection(option)) #Show the user what they're selecting
    return checker(option)

def upstatus(status):
    with open('status.txt','r') as rf: #Read the file and make changes
        contents = rf.read()
        if "bl=" in status:         #If it is a backlight update
            if "0" in status:
                contents = re.sub('backlight=.', 'backlight=0', contents)
            if "1" in status:
                contents = re.sub('backlight=.', 'backlight=1', contents)
        if "nw=" in status:         #If it is a network update
            if "NOR" in status:
                contents = re.sub('network=...', 'network=NOR', contents)
            if "BRI" in status:
                contents = re.sub('network=...', 'network=BRI', contents)
            if "HOT" in status:
                contents = re.sub('network=...', 'network=HOT', contents)
        if "ssh=" in status:        #If it is a ssh update
            if "0" in status:
                contents = re.sub('ssh=.', 'ssh=0', contents)
            if "1" in status:
                contents = re.sub('ssh=.', 'ssh=1', contents)
    #Write the update out to the file
    with open('status.txt','w+') as wf:
        wf.write(contents)
    return 0


def chkstatus(status):
    with open('status.txt','r') as cf: #Read the file and make changes
        contents = cf.read()
        if status in contents:
            result = 1
        if status not in contents:
            result = 0
    return result


#MAKES SURE ALL FUNCTIONS ARE DECLARED AND RETURNS TO THE TOP
if __name__ == '__main__':
    main()
