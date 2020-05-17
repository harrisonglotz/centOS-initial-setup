#!/user/bin/python3

import os 
import time

#update server
print('\n*****Getting updates...*****\n\n')
os.system('dnf check-update')
os.system('dnf update')
os.system('dnf clean all')

#install preferred packages
print('\n*****Getting preferred packages...*****\n\n')
os.system('dnf install openssh-server vim nano wget curl net-tools')
os.system('y')

#start SSH
print('*****Starting SSH...*****')
os.system('systemctl start ssh')
os.system('systemctl restart ssh')

#create new sudo user
print('*****Creating sudo user...*****')
username = input('Enter username for sudo user: ')
os.system(f'adduser {username}')
os.system(f'passwd {username}')
os.system(f'usermod -aG wheel {username}')

print('*****Set up script complete!*****')







