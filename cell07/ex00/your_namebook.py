#!/usr/bin/env python3

def array_of_names(persons):
    names = []

    for first, last in persons.items():
        full_name = first.capitalize() + " " + last.capitalize()
        names.append(full_name)

    return names


# Test
persons = {
    "jek": "jinfong",
    "gray": "gayta",
    "xavi": "porx",
    "fifee": "yingko"
}

print(array_of_names(persons))