# Create a terminal_game.py that walks the player through a captivating mini-game adventure! In each step of the adventure, the player should be presented with 2 or more options on where to go next.
# A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
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
print(f'Welcome aboard {rank} {name} from the {galaxy} Galaxy.')
print('Lets begin our mission...')
print('')

# Epic 1
print('Epic 1: The Initial Encounter...')
print('')
print('Your spaceship encounters a mysterious alien vessel in deep space...')
print('')
print('A: Approach the mysterious spaceship')
print('B: Hide behind an asteroid and observe.')
print('')

# Scene1
scene1 = input('Choose your fate: ')

# Scene 1 Logic
if scene1 == 'a' or scene1 == 'A':
  print('As your spaceship inches closer, the alien vessel’s lights flicker to life, revealing intricate designs and unfamiliar symbols')
  print('Suddenly, a holographic message projects into your cockpit, welcoming you aboard.')
  print('The aliens appear friendly and invite you to dock for a meeting.')
elif scene1 == 'b' or scene1 == 'B':
  print('You skillfully maneuver behind a nearby asteroid, observing the alien ship’s movements.')
  print('You notice a pattern in their patrol routes and detect a weak point in their defenses.')
  print('This information could be invaluable for future encounters.')
else:
  print('That is not an option, please try again.')
  input('Choose your fate: ')
print('')

# Epic 2
print('Epic 2: Alien Diplomacy...')
print('')
print('The aliens extend a diplomatic invitation after your initial contact...')
print('')
print('A: Accept the invitation to meet the alien leader.')
print('B: Decline and investigate their technology instead.')
print('')

# Scene 2
scene2 = input('Choose your fate: ')

# Scene 2 Logic
if scene2 == 'a' or scene2 == 'A':
  print('You are greeted warmly by the alien leader, who shares their knowledge of the tyrannical empire and proposes an alliance.')
  print('This new friendship could prove essential in your fight against the empire.')
elif scene2 == 'b' or scene2 == 'B':
  print('You decline the invitation and focus on studying their advanced technology.')
  print('You manage to hack into their systems, discovering blueprints for a powerful weapon that could turn the tide in your favor.')
else:
  print('That is not an option, please try again.')
  input('Choose your fate: ')
print('')

# Epic 3
print('Epic 3: The Secret Mission...')
print('')
print('You receive intel about an enemy base housing crucial information...')
print('')
print('A: Sneak into the enemy base to gather intelligence.')
print('B: Launch a direct assault on the enemy base.')
print('')

# Scene 3
scene3 = input('Choose your fate: ')

# Scene 3 Logic
if scene3 == 'a' or scene3 == 'A':
  print('Under the cover of darkness, you infiltrate the enemy base.')
  print('You gather crucial intel on the empire’s plans, including the location of their secret weapon.')
  print('Your stealthy approach ensures you remain undetected, setting the stage for a strategic advantage.')
elif scene3 == 'b' or scene3 == 'B':
  print('Leading a daring attack, you and your crew storm the enemy base.')
  print('The fierce battle results in heavy casualties on both sides, but you manage to capture vital enemy officers who divulge the empire’s next move.')
else:
  print('That is not an option, please try again.')
  input('Choose your fate: ')
print('')

# Epic 4
print('Epic 4: The Betrayal...')
print('')
print('A defecting enemy officer offers valuable information...')
print('')
print('A: Trust the defecting enemy officer’s intel.')
print('B: Capture the defecting officer for interrogation.')
print('')

# Scene 4
scene4 = input('Choose your fate: ')

# Scene 4 Logic
if scene4 == 'a' or scene4 == 'A':
  print('Taking a leap of faith, you believe the defecting officer’s information.')
  print('Their intel leads you to a hidden empire base, which you successfully sabotage, delaying the empire’s plans and gaining a crucial upper hand.')
elif scene4 == 'b' or scene4 == 'B':
  print('You detain the officer, extracting information through rigorous interrogation.')
  print('The officer’s intel reveals a plot within the empire to overthrow their own leaders, providing an opportunity to sow discord among your enemies.')
else:
  print('That is not an option, please try again.')
  input('Choose your fate: ')
print('')

# Epic 5
print('Epic 5: The Final Battle...')
print('')
print('The time has come for a decisive confrontation with the empire...')
print('')
print('A: Lead a coalition of alien civilizations against the empire.')
print('B: Launch a stealth mission to disable the empire’s superweapon.')
print('')

# Scene 5
scene5 = input('Choose your fate: ')

# Scene 5 Logic
if scene5 == 'a' or scene5 == 'A':
  print('Rallying your newfound allies, you lead a massive coalition fleet against the empire.')
  print('The combined might of diverse civilizations overwhelms the enemy, resulting in a decisive victory that liberates the galaxy from tyranny.')
elif scene5 == 'b' or scene5 == 'B':
  print('Opting for a covert approach, you and a select team infiltrate the empire’s superweapon facility.')
  print('With precise execution, you disable the weapon, preventing mass destruction and turning the tide of war in your favor.')
else:
  print('That is not an option, please try again.')
  input('Choose your fate: ')