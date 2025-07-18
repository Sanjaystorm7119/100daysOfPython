import random
# print(random.randint(1, 10))  # Generates a random integer between 1 and 10 both inclusive
# print(random.choice(['apple', 'banana', 'cherry']))  # Randomly selects an item from the list
# print(random.random())  # Generates a random float between 0.0 and 1.0
# print(random.uniform(1.0, 10.0))  # Generates a random float between 1.0 and 10.0 both inclusive
# print(random.sample(range(100), 5))  # Randomly selects 5 unique numbers
# print(random.random())  # Generates a random float between 0.0 and 1.0


#practice code
# toss = ["heads", "tails"]
# print(random.choice(toss))

heads_or_tails = random.randint(0,1)
print("Heads" if heads_or_tails == 0 else "Tails")
