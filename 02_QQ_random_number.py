# Quiz Quest Component 2 - Random Number Generator

import random

difficulty = input("What is difficulty? ").lower()
if difficulty == "e":
    high = 50
    low = 0
elif difficulty == "n":
    high = 100
    low = 0
else:
    high = 100
    low = -100


for item in range(1,20):
    secret = random.randint(low, high)
    print(secret, end = "\t")