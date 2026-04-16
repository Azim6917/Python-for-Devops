# functions in python

import os

def check(Enter_command):
    print(os.system(Enter_command))

print ("***** RAM USAGE *****")
check ("free")
print ("____________________________________________________________________________")
print ("***** DISK USAGE *****")
check ("df -h")
print ("____________________________________________________________________________")
print ("***** CURRENT OS *****")
check ("uname")