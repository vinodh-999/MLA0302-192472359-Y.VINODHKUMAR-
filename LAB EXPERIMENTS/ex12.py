import random

# Parameters
alpha = 0.5
gamma = 0.9
epsilon = 0.2

# States (Rooms)
states = [0, 1, 2, 3, 4]

# Actions
actions = ["LEFT", "RIGHT"]

# Q-table
Q = {}
for s in states:
    for a in actions:
        Q[(s, a)] = 0

goal = 4

# Choose action
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
        state = min(state + 1, goal)
    else:
        state = max(state - 1, 0)

    if state == goal:
        reward = 10      # Clean room
    else:
        reward = -1      # Energy used

    return state, reward

# Training
for episode in range(100):

    state = 0
    action = choose_action(state)

    while state != goal:

        next_state, reward = move(state, action)
        next_action = choose_action(next_state)

        # SARSA Update
        Q[(state, action)] = Q[(state, action)] + alpha * (
            reward + gamma * Q[(next_state, next_action)] - Q[(state, action)]
        )

        state = next_state
        action = next_action

print("Training Completed\n")

# Testing
state = 0
print("Robot Path:")

while state != goal:
    action = choose_action(state)
    print("Room", state, "->", action)
    state, reward = move(state, action)

print("Room", goal)
print("Cleaning Completed!")
