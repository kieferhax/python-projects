# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀
# 
# Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
earthWeight = float(input('Enter your weight on Earth: '))
# Asks the user for a planet number (as an int).
destinationPlanet = int(input('Enter a planet number: '))
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight:
# destination weight=Earth weight × relative gravity 
# 1 |	Mercury |	0.38
# 2	| Venus	  | 0.91
# 3	| Mars	  | 0.38
# 4	| Jupiter	| 2.53
# 5	| Saturn	| 1.07
# 6	| Uranus	| 0.89
# 7 | Neptune	| 1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
if destinationPlanet == 1:
  print(earthWeight*0.38)
elif destinationPlanet == 2:
  print(earthWeight*0.91)
elif destinationPlanet == 3:
  print(earthWeight*0.38)
elif destinationPlanet == 4:
  print(earthWeight*2.53)
elif destinationPlanet == 5:
  print(earthWeight*1.07)
elif destinationPlanet == 6:
  print(earthWeight*0.89)
elif destinationPlanet == 7:
  print(earthWeight*1.14)
else:
  print('Invalid planet number.')