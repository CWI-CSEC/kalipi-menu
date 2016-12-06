#!/usr/bin/env python

import os
import GUIbuttons
import CLIbuttons
import time
import subprocess

mode = os.popen('echo $DISPLAY').read().strip()

if mode:
	os.system('python ~/bin/GUIbuttons.py')
else:
        os.system('python ~/bin/CLIbuttons.py')