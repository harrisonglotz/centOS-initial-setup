#!/user/bin/python3

import os 
import time

#update server
os.system('dnf check-update')
os.system('dnf update')
time.sleep(15)
os.system('y')
os.system('dnf clean all')

#install preferred packages
os.system('dnf install vim nano wget curl net-tools')
os.system('')



