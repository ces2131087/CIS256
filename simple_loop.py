"""
Cesar Cervantes Lopez
Module 08 Lab Assignment
Part A

This program is made to be be placed into a GitHub Repo
"""
import math as math

x = 'hi'
b = 0


while x != 'stop':
    b += 1

    print('Welcome to the simple loop')
    print()

    print(f'I have executed {b} times')


    x = input('Type \'stop\' to exit the loop: ')
    print()

print(f'The loop iterated a total of {b} times')

#update made to file:
y = math.pi * b

print(f'{b} multiplied by pi is {y:.2f} rounded to the nearest hundreth.')