# Bellman Equation

gamma = 0.9

reward = [
    [-1, -1, -1],
    [-1, 5, -1],
    [-1, -1, 10]
]

rows = 3
cols = 3

value = [[0 for j in range(cols)] for i in range(rows)]

for iteration in range(10):

    new_value = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):

            new_value[i][j] = reward[i][j] + gamma * value[i][j]

    value = new_value

print("State Value Function\n")

for row in value:
    print(row)
