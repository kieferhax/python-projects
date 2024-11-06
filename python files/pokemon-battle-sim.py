import random

class Pokemon:
    def __init__(self, entry, name, level, height, weight, type, region, description, is_caught, hp, attack, defense, speed):
        self.entry = entry
        self.name = name
        self.level = level
        self.height = height
        self.weight = weight
        self.type = type
        self.region = region
        self.description = description
        self.is_caught = is_caught
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.status = None

    def speak(self):
        print(self.name + "! " + self.name + "!")

    def display_details(self):
        print("Entry Number: " + str(self.entry))
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("Height: " + str(self.height) + " centimeters")
        print("Weight: " + str(self.weight) + " lbs")
        print("Type: " + str(self.type))
        print("Region: " + self.region)
        print("Caught: " + str(self.is_caught))
        print("HP: " + str(self.hp))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Speed: " + str(self.speed))
        print("Description: " + str(self.description))
        if self.status:
            print("Status: " + self.status)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_pokemon(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")
        damage = self.calculate_damage(other_pokemon)
        other_pokemon.take_damage(damage)
        print(f"{other_pokemon.name} takes {damage} damage and now has {other_pokemon.hp} HP.")

    def calculate_damage(self, other_pokemon):
        # Simple damage calculation considering type advantage/disadvantage
        type_advantage = self.type_advantage(other_pokemon)
        damage = (self.attack - other_pokemon.defense) * type_advantage
        if damage < 0:
            damage = 0
        return damage

    def type_advantage(self, other_pokemon):
        # Simplified type advantage logic
        type_chart = {
            'Fire': {'weak': ['Water', 'Rock'], 'strong': ['Grass', 'Bug']},
            'Water': {'weak': ['Electric', 'Grass'], 'strong': ['Fire', 'Rock']},
            'Electric': {'weak': ['Ground'], 'strong': ['Water', 'Flying']},
            # Add more types as needed
        }
        advantage = 1
        for t in self.type:
            if t in type_chart:
                if any(weak in other_pokemon.type for weak in type_chart[t]['weak']):
                    advantage *= 0.5
                if any(strong in other_pokemon.type for strong in type_chart[t]['strong']):
                    advantage *= 2
        return advantage

    def apply_status_effect(self):
        if self.status == 'Poisoned':
            self.hp -= 5
            print(f"{self.name} is hurt by poison and loses 5 HP.")
        # Add more status effects as needed


def battle(pokemon1, pokemon2):
    print(f"Battle between {pokemon1.name} and {pokemon2.name}!")
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        if pokemon1.speed > pokemon2.speed:
            pokemon1.attack_pokemon(pokemon2)
            if pokemon2.hp > 0:
                pokemon2.attack_pokemon(pokemon1)
        else:
            pokemon2.attack_pokemon(pokemon1)
            if pokemon1.hp > 0:
                pokemon1.attack_pokemon(pokemon2)
        pokemon1.apply_status_effect()
        pokemon2.apply_status_effect()
        print()
    if pokemon1.hp > 0:
        print(f"{pokemon1.name} wins the battle!")
    else:
        print(f"{pokemon2.name} wins the battle!")

# Example Pokémon with battle attributes
raichu = Pokemon(26, 'Raichu', 50, 76.2, 66.1, ['Electric'], 'Alola', 'Its tail discharges electricity into the ground, protecting it from getting shocked.', True, 100, 55, 40, 90)
arcanine = Pokemon(59, 'Arcanine', 59, 190.5, 341.7, ['Fire'], 'Kanto', 'Its magnificent bark conveys a sense of majesty. Anyone hearing it can’t help but grovel before it.', False, 100, 60, 50, 80)

# Simulate a battle
battle(raichu, arcanine)
