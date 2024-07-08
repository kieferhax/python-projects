import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

total = dice1 + dice2
guess = 0

int(input('What is the total? '))

while guess != total:
  guess = int(input('What is the total? '))
print('You got it!')