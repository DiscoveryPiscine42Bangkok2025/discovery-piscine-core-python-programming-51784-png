#!/usr/bin/env python3

array = [2, 7, 9, 42, 8, 49, -17, 2]

new_array = []

for num in array:
    if num > 5:
        new_array.append(num + 2)

print(array)
print(new_array)