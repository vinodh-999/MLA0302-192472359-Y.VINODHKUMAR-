# GridWorld using Policy Iteration (Simple)

grid_size = 4

start = (0, 0)
goal = (3, 3)

# Obstacle
obstacle = (1, 1)

# Initial Policy
policy = {}

for i in range(grid_size):
    for j in range(grid_size):
        if (i, j) != goal:
            policy[(i, j)] = "RIGHT"

# Print Initial Policy
print("Initial Policy:\n")

for state in policy:
    print(state, "->", policy[state])

print("\nUpdating Policy...\n")

# Simple Policy Improvement
for state in policy:

    if state == obstacle:
        policy[state] = "BLOCK"

    elif state[0] < goal[0]:
        policy[state] = "DOWN"

    elif state[1] < goal[1]:
        policy[state] = "RIGHT"

    else:
        policy[state] = "GOAL"

# Display Final Policy
print("Optimal Policy:\n")

for state in sorted(policy):
    print(state, "->", policy[state])
