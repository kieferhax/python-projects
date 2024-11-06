import unittest
from pokemon_battle_simulator import Pokemon, battle

class TestPokemonBattleSimulator(unittest.TestCase):
    def setUp(self):
        self.raichu = Pokemon(26, 'Raichu', 50, 76.2, 66.1, ['Electric'], 'Alola', 'Its tail discharges electricity into the ground, protecting it from getting shocked.', True, 100, 55, 40, 90)
        self.arcanine = Pokemon(59, 'Arcanine', 59, 190.5, 341.7, ['Fire'], 'Kanto', 'Its magnificent bark conveys a sense of majesty. Anyone hearing it can’t help but grovel before it.', False, 100, 60, 50, 80)

    def test_pokemon_attributes(self):
        self.assertEqual(self.raichu.name, 'Raichu')
        self.assertEqual(self.raichu.hp, 100)
        self.assertEqual(self.arcanine.type, ['Fire'])

    def test_type_advantage(self):
        self.assertEqual(self.raichu.type_advantage(self.arcanine), 1)

    def test_calculate_damage(self):
        damage = self.raichu.calculate_damage(self.arcanine)
        self.assertGreater(damage, 0)

    def test_battle(self):
        winner = battle(self.raichu, self.arcanine)
        self.assertTrue(self.raichu.hp > 0 or self.arcanine.hp > 0)

if __name__ == '__main__':
    unittest.main()
