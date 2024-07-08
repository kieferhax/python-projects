guess = 0
tries = 0

while guess != 6 and tries < 3:
  guess = int(input("Guess the number: "))
  tries = tries + 1
if guess != 6:
  print('You ran out of tries')
else:
  print("You got it!")

# First, introduce a variable called tries at the top and give it a value of 0.

# Then, add the tries variable to the while loop using a relational operator (like you did with guess).