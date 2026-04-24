#!/usr/bin/env python3

def add_one(number):
    number += 1
    print("Inside method:", number)

# Variable in main program
x = 5

print("Before method:", x)

add_one(x)

print("After method:", x)