# Quiz Quest Component 2 - Random Number Generator

import random

low = 1
high = 50

for item in range(0,20):
    secret = random.randint(low, high)
    print(secret, end = "\t")