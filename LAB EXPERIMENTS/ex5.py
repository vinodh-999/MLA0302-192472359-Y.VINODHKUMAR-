# Value Iteration

gamma = 0.9

reward = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, 10]
]

rows = 3
cols = 3

V = [[0 for j in range(cols)] for i in range(rows)]

for iteration in range(10):

    newV = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            newV[i][j] = reward[i][j] + gamma * V[i][j]

    V = newV

print("Optimal Values")

for row in V:
    print(row)
