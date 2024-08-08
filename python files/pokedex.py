# Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters.
# A Pokédex is a device that tracks the information for Pokémon that are seen or caught. 
# Define a Pokemon class with the following attributes:
# entry (integer)
# name (string)
# type (list of strings)
# description (string)
# is_caught (boolean)

class Pokemon:
    def __init__(self, entry, name, level, height, weight, type, region, description, is_caught):
        self.entry = entry
        self.name = name
        self.level = level
        self.height = height
        self.weight = weight
        self.type = type
        self.region = region
        self.description = description
        self.is_caught = is_caught

# Next create an instance method called .speak() that prints a string of the sound a Pokemon makes.
# A Pokemon usually just says their name, so make the .speak() simply print out their name twice
    def speak(self):
        print(self.name)
        print(self.name)

# Create another instance method called .display_details() that prints the attributes of a Pokemon object
    def display_details(self):
        print(self.entry)
        print(self.name)
        print(self.level)
        print(self.height)
        print(self.weight)
        print(self.type)
        print(self.region)
        print(self.description)
        print(self.is_caught)

# Lastly create 3 Pokemon class objects and user the .speak() and .display_details() instance methods for each one
# Bonus: For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight.
raichu = Pokemon(26, 'Raichu', 50, 76.2, 66.1, ['Electric'], 'Alola', 'Its tail discharges electricity into the ground, protecting it from getting shocked.', True)
arcanine = Pokemon(59, 'Arcanine', 59, 190.5, 341.7, ['Fire'], 'Kanto', 'Its magnificent bark conveys a sense of majesty. Anyone hearing it can’t help but grovel before it.', False)
ninetales= Pokemon(38, 'Ninetales', 65, 109.22, 43.9, ['Fire'], 'Kanto', 'Some legends claim that each of its nine tails has its own unique type of special mystical power.', True)