#coding=utf-8
import os, sys, platform
 
os.system('xdg-open https://facebook.com/groups/1431748223768752/')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf refat.so refat32.so')
except:
    pass
os.system('rm -rf refat.so refat32.so')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('refat.so'):
        os.system('curl -L https://github.com/REFAT-156/Green/blob/main/refat.cpython-311.so?raw=true -o refat.so') 
        __import__("refat").rsbuy()
    else:
        __import__("refat").rsbuy()
 
elif bit == '32bit':
    if not os.path.isfile('refat32.so'):
        os.system('curl -L https://github.com/REFAT-156/Green/blob/main/refat32.cpython-311.so?raw=true -o refat32.so') 
        __import__("refat32").rsbuy()
    else:
        __import__("refat32").rsbuy()
