import random
import math

prices = [10, 15, 20]
counts = [0, 0, 0]
values = [0, 0, 0]

epsilon = 0.2
rounds = 100

print("Epsilon Greedy")

for i in range(rounds):

    if random.random() < epsilon:
        arm = random.randint(0, 2)
    else:
        arm = values.index(max(values))

    reward = prices[arm] + random.randint(-2, 2)

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Average Revenue:", values)

print("\nUCB")

counts = [1, 1, 1]
values = [10, 15, 20]

for t in range(3, rounds):

    ucb = []

    for i in range(3):
        score = values[i] + math.sqrt((2 * math.log(t)) / counts[i])
        ucb.append(score)

    arm = ucb.index(max(ucb))

    reward = prices[arm] + random.randint(-2, 2)

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Average Revenue:", values)

print("\nThompson Sampling")

success = [1, 1, 1]
failure = [1, 1, 1]

for i in range(rounds):

    samples = []

    for j in range(3):
        samples.append(random.betavariate(success[j], failure[j]))

    arm = samples.index(max(samples))

    reward = prices[arm] + random.randint(-2, 2)

    if reward > 15:
        success[arm] += 1
    else:
        failure[arm] += 1

print("Success:", success)
print("Failure:", failure)
