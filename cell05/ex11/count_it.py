#!/usr/bin/env python3

import sys

# Remove script name from arguments
params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print("parameters:", len(params))
    
    for param in params:
        print(param, len(param))