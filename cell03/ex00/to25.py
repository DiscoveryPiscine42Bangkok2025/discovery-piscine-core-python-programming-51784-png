#!/usr/bin/env python3

number = int(input("Enter a number: "))

if number > 25:
    print("Error")
else:
    for i in range(number, 26):
        print(i)