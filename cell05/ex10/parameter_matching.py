#!/usr/bin/env python3

import sys

# Check for exactly one parameter
if len(sys.argv) != 2:
    print("none")
else:
    expected_word = sys.argv[1]
    user_word = input("Enter a word: ")

    if user_word == expected_word:
        print("Good job!")
    else:
        print("Nope, sorry...")