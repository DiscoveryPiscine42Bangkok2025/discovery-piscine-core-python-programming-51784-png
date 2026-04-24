#!/usr/bin/env python3

def average(students):
    return sum(students.values()) / len(students)

# Test
class_3B = {
    "marine": 20,
    "jean": 42,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 5,
    "julie": 11,
    "marc": 49,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")