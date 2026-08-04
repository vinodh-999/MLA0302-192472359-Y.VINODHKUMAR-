import random

actions = ["Buy", "Hold", "Sell"]

policy = [0.33, 0.34, 0.33]

for episode in range(20):

    action = random.choices(actions, weights=policy)[0]

    reward = random.choice([1, -1])

    if action == "Buy" and reward == 1:
        policy[0] += 0.02
    elif action == "Hold" and reward == 1:
        policy[1] += 0.02
    elif action == "Sell" and reward == 1:
        policy[2] += 0.02

    total = sum(policy)
    policy = [p / total for p in policy]

print("Final Policy")

for i in range(3):
    print(actions[i], ":", round(policy[i], 2))
