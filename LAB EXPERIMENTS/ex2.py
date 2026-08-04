# Policy Evaluation

gamma = 0.9

rewards = [
    [0, 0, 2],
    [0, -2, 0],
    [0, 0, 5]
]

rows = 3
cols = 3

V = [[0 for j in range(cols)] for i in range(rows)]

for iteration in range(10):
    newV = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            newV[i][j] = rewards[i][j] + gamma * V[i][j]

    V = newV

print("State Value Function")

for row in V:
    print(row)
