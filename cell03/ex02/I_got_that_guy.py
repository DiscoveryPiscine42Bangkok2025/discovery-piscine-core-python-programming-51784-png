#!/usr/bin/env python3

user_input = ""

while user_input != "STOP":
    user_input = input("Say something (type STOP to quit): ")
    
    if user_input != "STOP":
        print("I got that!")