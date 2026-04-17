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

'''take input from user '''

name = input("Enter the name: ")

def greet(name):
    print ("Hello", name)

greet(name)

'''Problem 2
Write a function called find_maximum that takes two numbers as arguments and returns the larger of the two.

Example Input: find_maximum(4, 9)
Expected Output: 9'''

def find_maximum(num1, num2):
    if num1 > num2:
        print(num1) 
    else:
        print(num2)
        
find_maximum(11, 9)