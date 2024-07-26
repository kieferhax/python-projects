# Ever wonder how many people live in New York City? What about London?
# Create a favorite-cities.py program
# Let's make a City class that uses the __init__() method to define the following attributes:
# name (string)
# country (string)
# population (integer rounded to the nearest thousand people)
# landmarks (list of strings)
class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

# Next create an object for you hometown and assign the attributes above
Ridgecrest = City('Ridgecrest', 'United States of America', 28346, ['China Lake Naval Weapons Center', 'China Lake Air and Space Museum', 'Maturango Museum'])
# Lastly, create another object of the city that you're always wanted to visit!
Osaka = City('Osaka', 'Japan', 2691000, ['Hidden Osaka', 'Osaka Castle', 'Dotonbori'])

print(vars(Ridgecrest))
print(vars(Osaka))
