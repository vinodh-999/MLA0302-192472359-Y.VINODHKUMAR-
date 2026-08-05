import random

# Sample stock prices
prices = [100, 102, 101, 105, 108, 110, 107, 112]

actions = ["Buy", "Sell", "Hold"]

balance = 1000
stock = 0

print("Double DQN Stock Trading Simulation\n")

for i in range(len(prices)):

    price = prices[i]

    # Random action (simulating Double DQN decision)
    action = random.choice(actions)

    print("Day", i + 1)
    print("Price =", price)
    print("Action =", action)

    if action == "Buy" and balance >= price:
        stock += 1
        balance -= price
        print("Bought Stock")

    elif action == "Sell" and stock > 0:
        stock -= 1
        balance += price
        print("Sold Stock")

    else:
        print("Hold Position")

    print("Balance =", balance)
    print("Stocks =", stock)
    print()

total_value = balance + stock * prices[-1]

print("Final Balance =", balance)
print("Stocks Left =", stock)
print("Portfolio Value =", total_value)
