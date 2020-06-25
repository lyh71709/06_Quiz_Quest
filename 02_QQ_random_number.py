# Quiz Quest Component 2 - Random Number Generator

import random

# Low and hogh is set
low = 1
high = 4

# For loop loops 20 times to get all the numbers between 1 and 4 to get printed
for item in range(0,20):
    secret = random.randint(low, high)
    print(secret, end = "\t")