# Autonomous Car Navigation

road = [
    ["S", ".", "."],
    [".", "R", "."],
    [".", ".", "G"]
]

x = 0
y = 0

reward = 0

print("Car Navigation\n")

while True:

    print("Position:", (x, y))

    if road[x][y] == "R":
        print("Red Signal - Stop")

    if (x, y) == (2, 2):
        reward += 10
        print("Destination Reached")
        break

    reward += 1

    if y < 2:
        y += 1
    else:
        x += 1

print("Total Reward =", reward)
