#!/user/bin/python3

import os 
import time

#update server
print('\nGetting updates...\n\n')
os.system('dnf check-update')
os.system('dnf update')
time.sleep(15)
os.system('y')
os.system('dnf clean all')

print('\nGetting preferred packages...\n\n')
#install preferred packages
os.system('dnf install openssh-server vim nano wget curl net-tools')
os.system('y')



