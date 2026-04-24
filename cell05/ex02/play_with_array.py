#!/usr/bin/env python3

# Original array
original_array = [2, 7, 9, 42, 8, 49, -17, 2]

# New array: only values greater than 5, then add 2
new_array = []

for num in original_array:
    if num > 5:
        new_array.append(num + 2)

# Display arrays
print(original_array)
print(new_array)