#!/usr/bin/env python3

def find_the_redheads(family):
    return list(
        map(
            lambda person: person[0],
            filter(lambda person: person[1] == "red", family.items())
        )
    )

# Test
dupont_family = {
    "Billow": "red",
    "marie": "blond",
    "virginie": "brunette",
    "Krixi": "red",
    "omen": "red"
}

print(find_the_redheads(dupont_family))