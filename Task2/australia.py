from constraint import Problem

# Create CSP problem
problem = Problem()

# Regions of Australia
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Available colours
colors = ["Red", "Green", "Blue"]

# Add variables
for region in regions:
    problem.addVariable(region, colors)

# Define neighboring regions
neighbors = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V")
]

# Constraint:
# Neighboring regions cannot have same colour
for region1, region2 in neighbors:
    problem.addConstraint(
        lambda a, b: a != b,
        (region1, region2)
    )

# Solve problem
solution = problem.getSolution()

# Display solution
print("Australia Map Coloring Solution")
print("--------------------------------")

for region in regions:
    print(f"{region}: {solution[region]}")