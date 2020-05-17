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
os.system('dnf install openssh-server vim nano wget net-tools')

#start SSH
print('\n*****Starting SSH...*****\n\n')
os.system('systemctl start sshd')
os.system('systemctl restart sshd')

#create new sudo user
print('\n*****Creating sudo user...*****\n\n')
username = input('Enter username for sudo user: ')
os.system(f'adduser {username}')
os.system(f'passwd {username}')
os.system(f'usermod -aG wheel {username}')

print('*****Set up script complete!*****')







