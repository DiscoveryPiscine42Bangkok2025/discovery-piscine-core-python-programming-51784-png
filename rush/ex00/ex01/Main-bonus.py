#!/usr/bin/env python3

import sys
from Bonus import king_in_check


def read_board(filename):
    try:
        with open(filename,"r") as f:
            return [line.strip() for line in f]
    except:
        return None


if len(sys.argv) < 2:
    sys.exit()

for file in sys.argv[1:]:
    board = read_board(file)

    if board is None:
        print("Error")
        continue

    result = king_in_check(board)

    if result is None:
        print("Error")
    else:
        print("Success")