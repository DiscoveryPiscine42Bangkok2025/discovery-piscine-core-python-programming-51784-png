#!/usr/bin/env python3

import sys

params = sys.argv[1:]

# If no parameters
if len(params) == 0:
    print("none")
else:
    found = False

    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")
            found = True

    # If all parameters already ended with "ism"
    if not found:
        print("none")