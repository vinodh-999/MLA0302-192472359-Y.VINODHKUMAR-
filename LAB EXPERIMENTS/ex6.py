import random
import math

ads = [0.2, 0.5, 0.8]
rounds = 100

print("Epsilon Greedy")

epsilon = 0.1
count = [0, 0, 0]
value = [0, 0, 0]

for i in range(rounds):

    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = value.index(max(value))

    reward = 1 if random.random() < ads[ad] else 0

    count[ad] += 1
    value[ad] += (reward - value[ad]) / count[ad]

print("CTR:", value)

print("\nUCB")

count = [1, 1, 1]
value = [0.2, 0.5, 0.8]

for t in range(3, rounds):

    score = []

    for i in range(3):
        score.append(value[i] + math.sqrt((2 * math.log(t)) / count[i]))

    ad = score.index(max(score))

    reward = 1 if random.random() < ads[ad] else 0

    count[ad] += 1
    value[ad] += (reward - value[ad]) / count[ad]

print("CTR:", value)

print("\nThompson Sampling")

success = [1, 1, 1]
failure = [1, 1, 1]

for i in range(rounds):

    sample = []

    for j in range(3):
        sample.append(random.betavariate(success[j], failure[j]))

    ad = sample.index(max(sample))

    reward = 1 if random.random() < ads[ad] else 0

    if reward == 1:
        success[ad] += 1
    else:
        failure[ad] += 1

print("Success:", success)
print("Failure:", failure)
