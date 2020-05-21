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
os.system('dnf install openssh-server sudo vim nano wget net-tools')

#start SSH
print('\n*****Starting SSH...*****\n\n')
os.system('systemctl start sshd')
os.system('systemctl restart sshd')

#change timezone to Standard Est. Time
print('\n=====Setting Timezone=====\n\n')
os.system('timedatectl set-timezone America/New_York')
os.system('timedatectl status')

#create new sudo user
print('\n*****Creating sudo user...*****\n\n')
username = input('Enter username for sudo user: ')
os.system(f'adduser {username}')
os.system(f'passwd {username}')
os.system(f'usermod -aG wheel {username}')

print('*****Set up script complete!*****')







