#!/usr/bin/env python3

def famous_births(figures):
    # Sort by date of birth
    sorted_figures = sorted(
        figures.values(),
        key=lambda person: int(person["date_of_birth"])
    )

    for person in sorted_figures:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")


# Test
women_scientists = {
    "ada": { "name": "Marie Curie", "date_of_birth": "1867" },
    "cecilia": { "name": "Rosalind Franklin", "date_of_birth": "1920" },
    "lise": { "name": "Chien-Shiung Wu ", "date_of_birth": "1912" },
    "grace": { "name": "Jane Goodall", "date_of_birth": "1934" }
}

famous_births(women_scientists)