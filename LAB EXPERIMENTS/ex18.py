import random

# Machine settings
actions = ["Low", "Medium", "High"]

# Rewards for each setting
reward_table = {
    "Low": 4,
    "Medium": 8,
    "High": 6
}

# Initialize value function
Q = {a: 0 for a in actions}

alpha = 0.1
epsilon = 0.2

episodes = 100

for episode in range(episodes):

    # Epsilon-Greedy Policy
    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        action = max(Q, key=Q.get)

    reward = reward_table[action]

    # Update Value Function
    Q[action] = Q[action] + alpha * (reward - Q[action])

print("Learned Value Function")
for action in actions:
    print(action, ":", round(Q[action], 2))

best = max(Q, key=Q.get)
print("\nBest Machine Setting:", best)
