import random

episodes = 100

returns = []

for episode in range(episodes):

    # Simulated reward
    # +1 = Customer stays
    # 0 = Customer leaves

    reward = random.choice([0, 1])

    returns.append(reward)

value = sum(returns) / len(returns)

print("Estimated Policy Value:", round(value, 2))

print("\nAnalysis")
if value > 0.5:
    print("Policy performs well.")
else:
    print("Policy needs improvement.")
