#!/usr/bin/env python3

import sys

# If fewer than 2 parameters (excluding script name)
if len(sys.argv) < 3:
    print("none")
else:
    # Print parameters in reverse order
    for arg in reversed(sys.argv[1:]):
        print(arg)