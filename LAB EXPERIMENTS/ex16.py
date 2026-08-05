import random

# Energy production (units)
production = [80, 100, 120]

# Energy demand (units)
demand = [70, 90, 110]

# Total cost
total_cost = 0

print("Smart Grid Energy Management\n")

for i in range(5):

    p = random.choice(production)
    d = random.choice(demand)

    # Cost calculation
    if p >= d:
        cost = (p - d) * 2      # Extra energy storage cost
        status = "Balanced"
    else:
        cost = (d - p) * 5      # Energy shortage cost
        status = "Shortage"

    total_cost += cost

    print("Hour:", i + 1)
    print("Production:", p)
    print("Demand:", d)
    print("Status:", status)
    print("Cost:", cost)
    print()

print("Total Cost:", total_cost)

if total_cost < 100:
    print("Policy Optimized Successfully!")
else:
    print("Need Better Energy Management.")
