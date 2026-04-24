#!/usr/bin/env python3

import sys

# Check for exactly 2 parameters (excluding script name)
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)