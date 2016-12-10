#!/usr/bin/env python

#################################################
# Make sure these files are in the same directory
#################################################
# HOTinterfaces
# HOThostapd.conf
# BRIhostapd.conf
# BRIinterfaces
# hostapd.conf
# TUNssh.socket
# TUNsshd_config



import os
import re
import subprocess


os.popen('clear').read().strip()
print "Starting install"
choice = raw_input("Do you already have Re4son for your Pi? Y/N   ")
if choice == "N" or choice == "n" or choice == "NO" or choice == "no" or choice == "No":
    print "Installing Re4son"
    print "NOTE: You will have to reboot and run this install again"
    print "NOTE: DO NOT REBOOT WHEN PROMPTED OR YOU WILL HAVE TO REPEAT IT"
    print "NOTE: THE SYSTEM WILL REBOOT ON ITS OWN"
    os.popen('mount /dev/mmcblk0p1 /boot').read().strip()
    os.popen('cd /usr/local/src').read().strip()
    os.popen('wget  -O re4son_kali-pi-tft_kernel_current.tar.xz https://whitedome.com.au/re4son/downloads/10452/').read().strip()
    os.popen('tar -xJf re4son_kali-pi-tft_kernel_current.tar.xz').read().strip()
    os.popen('cd re4son_kali-pi-tft_kernel_4*').read().strip()
    os.popen('chmod +x install.sh').read().strip()
    os.popen('./install.sh').read().strip()
    os.popen('./re4son-pi-tft-setup -d').read().strip()
    os.popen('./re4son-pi-tft-setup -t 22 -u /root').read().strip()
    print "The system will now reboot..."
    os.popen('reboot').read().strip()
print "Installing requirements"
print "[Step 1/8]"
subprocess.Popen('apt-get install -y hostapd', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
print "[Step 2/8]"
os.popen('apt-get -y install dnsmasq').read().strip()
print "[Step 3/8]"
os.popen('apt-get -y install python-dev').read().strip()
print "[Step 4/8]"
os.popen('apt-get -y install hostapd gcc').read().strip()
print "[Step 5/8]"
os.popen('apt-get -y install python-pygame').read().strip()
print "[Step 6/8]"
os.popen('wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz').read().strip()
print "[Step 7/8]"
os.popen('tar zxvf RPi.GPIO-0.5.11.tar.gz').read().strip()
print "Starting RPIO setup"
print "[Step 8/8]"
os.popen('python RPi.GPIO-0.5.11/setup.py install').read().strip()
print "Starting setup for menu:"
os.popen('cd ..').read().strip()
hotspot = raw_input("Hotspot name[MiPi]: ")
password = raw_input("Hotspot password[Password11]: ")
#Write to the hotspot file
f = open('config/HOThostapd.conf', 'r')
contents = f.read()
contents = re.sub('ssid=[a-z]{1,32}[A-Z]{1,32}[0-9]{1,32}/[$-/:-?{-~!"^_`\[\]]/{1,32}', 'ssid=%s'%hotspot, contents)
contents = re.sub('wpa_passphrase=[a-z]{1,32}[A-Z]{1,32}[0-9]{1,32}/[$-/:-?{-~!"^_`\[\]]/{1,32}', 'wpa_passphrase=%s'%password, contents)
f.close()
f = open('config/HOThostapd.conf', 'w')
f.write(contents)
f.close()
#Write to the bridged hotspot file
f = open('config/BRIhostapd.conf', 'r')
contents = f.read()
contents = re.sub('ssid=[a-z]{1,32}[A-Z]{1,32}[0-9]{1,32}/[$-/:-?{-~!"^_`\[\]]/{1,32}', 'ssid=%s'%hotspot, contents)
contents = re.sub('wpa_passphrase=[a-z]{1,32}[A-Z]{1,32}[0-9]{1,32}/[$-/:-?{-~!"^_`\[\]]/{1,32}', 'wpa_passphrase=%s'%password, contents)
f.close()
f = open('config/BRIhostapd.conf', 'w')
f.write(contents)
f.close()
print "Copying files"
os.popen('cp -i /etc/network/interfaces /etc/network/NORMinterfaces').read().strip()
os.popen('cp -i config/HOTinterfaces /etc/network/HOTinterfaces').read().strip()
os.popen('cp -i config/BRIinterfaces /etc/network/BRIinterfaces').read().strip()
os.popen('mkdir /etc/hostapd').read().strip()
os.popen('cp -i config/BRIhostapd.conf /etc/hostapd/BRIhostapd.conf').read().strip()
os.popen('cp -i config/HOThostapd.conf /etc/hostapd/HOThostapd.conf').read().strip()
os.popen('cp -i config/hostapd.conf /etc/hostapd/hostapd.conf').read().strip()
os.popen('cp -i /lib/systemd/system/ssh.socket /lib/systemd/system/NORMssh.socket').read().strip()
os.popen('cp -i config/TUNssh.socket /lib/systemd/system/TUNssh.socket').read().strip()
os.popen('cp -i /etc/ssh/sshd_config /etc/ssh/NORMsshd_config').read().strip()
os.popen('cp -i config/TUNsshd_config /etc/ssh/TUNsshd_config').read().strip()
os.popen('clear').read().strip()
print "Complete!"
print "Steps to take:"
print "Manually setup 'menu.py' for SSH by setting the variables"
print "Setup your hotspot (both tunneling hotspot and bridged) using the hostapd file"
print "END"
