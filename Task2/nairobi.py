from constraint import Problem

# Create problem
problem = Problem()

# Nairobi sub-counties
subcounties = [
    "Westlands",
    "Dagoretti_North",
    "Dagoretti_South",
    "Langata",
    "Kibra",
    "Kasarani",
    "Embakasi_East",
    "Embakasi_West",
    "Embakasi_South",
    "Embakasi_North",
    "Embakasi_Central",
    "Makadara",
    "Kamukunji",
    "Starehe",
    "Mathare",
    "Roysambu",
    "Ruaraka"
]

# Colours
colors = ["Red", "Green", "Blue", "Yellow"]

# Add variables
for subcounty in subcounties:
    problem.addVariable(subcounty, colors)

# Neighbor relationships
neighbors = [

    ("Westlands", "Dagoretti_North"),
    ("Westlands", "Starehe"),
    ("Westlands", "Roysambu"),

    ("Dagoretti_North", "Dagoretti_South"),
    ("Dagoretti_North", "Kibra"),

    ("Dagoretti_South", "Langata"),

    ("Langata", "Kibra"),

    ("Kasarani", "Roysambu"),
    ("Kasarani", "Ruaraka"),
    ("Kasarani", "Embakasi_North"),

    ("Embakasi_North", "Embakasi_Central"),
    ("Embakasi_Central", "Embakasi_East"),
    ("Embakasi_Central", "Embakasi_West"),
    ("Embakasi_West", "Embakasi_South"),

    ("Makadara", "Kamukunji"),
    ("Kamukunji", "Starehe"),
    ("Mathare", "Ruaraka"),
]

# Constraints
for area1, area2 in neighbors:
    problem.addConstraint(
        lambda a, b: a != b,
        (area1, area2)
    )

# Solve
solution = problem.getSolution()

# Print result
print("Nairobi Sub-County Coloring")
print("--------------------------------")

for subcounty in subcounties:
    print(f"{subcounty}: {solution[subcounty]}")