# Simulate a coin toss
# 50% of the time, it's Head's
# 50% of the time, it's Tail's

import random

num = random.randint(0,1) # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')