# Policy Iteration (Simple)

grid_size = 4

policy = [['R' for j in range(grid_size)] for i in range(grid_size)]

value = [[0 for j in range(grid_size)] for i in range(grid_size)]

goal = (3, 3)

gamma = 0.9

for iteration in range(10):

    for i in range(grid_size):
        for j in range(grid_size):

            if (i, j) == goal:
                value[i][j] = 10
            else:
                value[i][j] = -1 + gamma * value[i][j]

print("Optimal Policy")

for row in policy:
    print(row)

print("\nValue Function")

for row in value:
    print(row)
