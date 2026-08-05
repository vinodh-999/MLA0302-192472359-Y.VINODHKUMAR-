import random

# Three learning courses
courses = ["Python", "AI", "Data Science"]

# True click rewards
true_reward = {
    "Python": 4,
    "AI": 8,
    "Data Science": 6
}

Q = {c: 0 for c in courses}
count = {c: 0 for c in courses}

epsilon = 0.1
runs = 200

total_reward = 0

for i in range(runs):

    # Explore
    if random.random() < epsilon:
        action = random.choice(courses)

    # Exploit
    else:
        action = max(Q, key=Q.get)

    reward = true_reward[action]

    total_reward += reward

    count[action] += 1

    # Incremental Average
    Q[action] = Q[action] + (reward - Q[action]) / count[action]

print("Average Rewards")
for c in courses:
    print(c, ":", round(Q[c], 2))

print("\nRecommendation Counts")
for c in courses:
    print(c, ":", count[c])

print("\nTotal Reward:", total_reward)

best = max(Q, key=Q.get)
print("Best Recommended Course:", best)
