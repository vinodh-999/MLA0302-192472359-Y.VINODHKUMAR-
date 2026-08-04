import random

episodes = 100

total_reward = 0

for episode in range(episodes):

    reward = random.choice([0, 1])

    total_reward += reward

average = total_reward / episodes

print("Episodes =", episodes)
print("Average Value =", average)
