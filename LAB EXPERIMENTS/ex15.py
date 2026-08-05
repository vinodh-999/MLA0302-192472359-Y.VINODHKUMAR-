import random

# Customer Service Representatives
agents = ["Agent A", "Agent B", "Agent C"]

# Initial Q-values
Q = {"Agent A": 0, "Agent B": 0, "Agent C": 0}

# Number of times each agent is selected
count = {"Agent A": 0, "Agent B": 0, "Agent C": 0}

# Simulate 20 customer calls
episodes = 20

for i in range(episodes):

    # Select an agent randomly
    agent = random.choice(agents)

    # Simulated call handling time (minutes)
    handling_time = random.randint(2, 8)

    # Reward (Less time = Higher reward)
    reward = 10 - handling_time

    # Update count
    count[agent] += 1

    # Monte Carlo Update (Average Reward)
    Q[agent] = Q[agent] + (reward - Q[agent]) / count[agent]

# Display Results
print("Average Rewards\n")

for agent in agents:
    print(agent, ":", round(Q[agent], 2))

# Best Agent
best_agent = max(Q, key=Q.get)

print("\nBest Representative:", best_agent)
