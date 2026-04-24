#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + ('Z' * (8 - len(text))))

params = sys.argv[1:]

if len(params) < 1:
    print("none")
else:
    for arg in params:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)