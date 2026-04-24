#!/usr/bin/env python3

import sys

# Check for exactly two parameters
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # Include both numbers in the range
    if start <= end:
        numbers = list(range(start, end + 1))
    else:
        numbers = list(range(start, end - 1, -1))

    print(numbers)