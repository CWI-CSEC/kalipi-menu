#!/bin/bash

clear
echo "Starting install..."
echo -n "Do you already have Re4son for your Pi? Y/N   "
read choice
if [[ $choice =~ ^[Nn]$ ]]; then
  echo "Installing Re4son"
  echo "NOTE: You will have to reboot and run this installer again"
  echo "NOTE: DO NOT REBOOT WHEN PROMPTED OR YOU WILL HAVE TO REPEAT IT"
  echo "NOTE: THE SYSTEM WILL REBOOT ON ITS OWN"
  sleep 5
  mount /dev/mmcblk0p1 /boot
  cd /usr/local/src
  wget  -O re4son_kali-pi-tft_kernel_current.tar.xz https://whitedome.com.au/re4son/downloads/11299/
  check=$(sha256sum re4son_kali-pi-tft_kernel_current.tar.xz | cut -d' ' -f1)
   if [ $check = "e7204e9fceffc8e9a99a84e6b0f84c8c9847e508346240c5e8e756d70e6b90af" ]; then
	echo "Checksum confirmed for Re4son kernel, 2017.10.31."
	echo "Proceeding."
   else
	echo "CHECKSUM ERROR."
	echo "Please check your network connection and try again."
	echo "Alternatively, try installing Re4son manually."
	echo "A guide can be found at http://whitedome.com.au/re4son/sticky-fingers-kali-pi/"
	echo "This script will now terminate."
	exit 1
   fi
  tar xvf re4son_kali-pi-tft_kernel_current.tar.xz
  cd re4son-kernel_4*
  chmod +x install.sh
  ./install.sh
  ./re4son-pi-tft-setup -t 22 -d /root
  ./re4son-pi-tft-setup -t 22 -u /root
  echo "The Re4son install is complete"
  echo "After the reboot, start the installer again"
  sleep 5
  reboot
fi
echo "Skipping Re4son software..."
echo "Installing requirements"
echo "-------------"
echo "[Step 1/8]"
echo "-------------"
apt-get -y install hostapd
echo "-------------"
echo "[Step 2/8]"
echo "-------------"
apt-get -y install dnsmasq
echo "-------------"
echo "[Step 3/8]"
echo "-------------"
apt-get -y install python-dev python-pip
echo "-------------"
echo "[Step 4/8]"
echo "-------------"
apt-get -y install hostapd gcc
echo "-------------"
echo "[Step 5/8]"
echo "-------------"
apt-get -y install python-pygame
echo "-------------"
echo "[Step 6/8]"
echo "-------------"
wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz
echo "-------------"
echo "[Step 7/8]"
echo "-------------"
tar zxvf RPi.GPIO-0.5.11.tar.gz
echo "-------------"
echo "Starting RPIO setup"
echo "[Step 8/8]"
echo "-------------"
cd RPi.GPIO-0.5.11/
python setup.py install
easy_install uinput
echo "Starting setup for menu:"
cd ..
rm -rf RPi.GPIO-0.5.11.tar.gz #Delete the zipped package
echo -n "Hotspot name[MiPi]: "
read hotspot
echo -n "Hotspot password[Password11]: "
read password
#Write to the hotspot file
sed -i "s/ssid=.*/ssid=$hotspot/g" config/HOThostapd.conf
sed -i "s/wpa_passphrase=.*/wpa_passphrase=$password/g" config/HOThostapd.conf
#ALso write to the bridged file
sed -i "s/ssid=.*/ssid=$hotspot/g" config/BRIhostapd.conf
sed -i "s/wpa_passphrase=.*/wpa_passphrase=$password/g" config/BRIhostapd.conf
echo "Copying files"
cp -i /etc/network/interfaces /etc/network/NORMinterfaces
cp -i config/HOTinterfaces /etc/network/HOTinterfaces
cp -i config/BRIinterfaces /etc/network/BRIinterfaces
mkdir /etc/hostapd
cp -i config/BRIhostapd.conf /etc/hostapd/BRIhostapd.conf
cp -i config/HOThostapd.conf /etc/hostapd/HOThostapd.conf
cp -i config/hostapd.conf /etc/hostapd/hostapd.conf
cp -i /lib/systemd/system/ssh.socket /lib/systemd/system/NORMssh.socket
cp -i config/TUNssh.socket /lib/systemd/system/TUNssh.socket
cp -i /etc/ssh/sshd_config /etc/ssh/NORMsshd_config
cp -i config/TUNsshd_config /etc/ssh/TUNsshd_config
echo "-------------"
echo "Complete!"
echo "Steps to take: Manually setup 'menu.py' for SSH by setting the variables"
echo "Setup your hotspot (both tunneling hotspot and bridged) using the hostapd file"
echo "FINAL STEP: Run these commands if there were any failures:"
echo "cd RPi.GPIO-0.5.11"
echo "python setup.py install"
echo "END"
echo "-------------"
