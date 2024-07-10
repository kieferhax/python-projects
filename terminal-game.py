# Create a terminal_game.py that walks the player through a captivating mini-game adventure! In each step of the adventure, the player should be presented with 2 or more options on where to go next.

# A space-based adventure of a crew of curious individuals exploring an unknown galaxy.

# Star Wars themed intro
from time import time


print('* * * * * * * * * * * * * * * * * *')
print('         SPACE ADVENTURES          ')
print('* * * * * * * * * * * * * * * * * *')
print('')
print('A not so very long time ago, in a not so very far away galaxy...')
print('Among the distant stars, a daring saga unfolds...')
print('Navigate cosmic battlegrounds...')
print('Meet mysterious alien civilizations...')
print('Unite against a tyrannical empire threatening to plunge the galaxy into darkness...')
print('')
print('* * * * * * * * * * * * * * * * * *')
print('')
# Get player name, rank, and location
name = input('Enter your name, cadet: ')
rank = input('Enter your rank: ')
galaxy = input('Enter your home galaxy: ')
print('                                                                                     ')
print(f'Welcome aboard {rank} {name} from the {galaxy} Galaxy. Lets begin our mission...')
print('')
# Epic 1
print('Epic 1: The Initial Encounter...')
print('')
print('Your spaceship encounters a mysterious alien vessel in deep space...')
print('A: Approach the mysterious spaceship')
print('B: Hide behind an asteroid and observe.')
# Scene1
scene1 = input('Choose your fate: ')
if scene1 == a or scene1 = A:
  print('As your spaceship inches closer, the alien vessel’s lights flicker to life, revealing intricate designs and unfamiliar symbols')
  print('Suddenly, a holographic message projects into your cockpit, welcoming you aboard.')
  print('The aliens appear friendly and invite you to dock for a meeting.')
elif scene1 == 'b' or 'B':
  print('You skillfully maneuver behind a nearby asteroid, observing the alien ship’s movements.')
  print('You notice a pattern in their patrol routes and detect a weak point in their defenses.')
  print('This information could be invaluable for future encounters.')
else:
  input('That is not an option, please try again.')