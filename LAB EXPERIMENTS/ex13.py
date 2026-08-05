import random

# Parameters
alpha = 0.5
gamma = 0.9
epsilon = 0.2

# Grid positions (0 to 4)
states = [0, 1, 2, 3, 4]

# Actions
actions = ["LEFT", "RIGHT"]

# Rewards
food = 4      # Goal
ghost = 2     # Penalty

# Q-table
Q = {}
for s in states:
    for a in actions:
        Q[(s, a)] = 0

# Choose action (Epsilon-Greedy)
def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    else:
        if Q[(state, "LEFT")] > Q[(state, "RIGHT")]:
            return "LEFT"
        else:
            return "RIGHT"

# Environment
def move(state, action):
    if action == "RIGHT":
        state = min(state + 1, 4)
    else:
        state = max(state - 1, 0)

    if state == food:
        reward = 10
    elif state == ghost:
        reward = -10
    else:
        reward = -1

    return state, reward

# Training
for episode in range(100):

    state = 0

    while state != food:

        action = choose_action(state)

        next_state, reward = move(state, action)

        # Q-Learning Update
        best_next = max(Q[(next_state, "LEFT")], Q[(next_state, "RIGHT")])

        Q[(state, action)] = Q[(state, action)] + alpha * (
            reward + gamma * best_next - Q[(state, action)]
        )

        state = next_state

print("Training Completed\n")

# Testing
state = 0

print("Agent Path:")

while state != food:

    if Q[(state, "LEFT")] > Q[(state, "RIGHT")]:
        action = "LEFT"
    else:
        action = "RIGHT"

    print("Position", state, "->", action)

    state, reward = move(state, action)

print("Position", food)
print("Food Collected!")
