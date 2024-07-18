# Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers.
# They are served in restaurants in the U.S. and Canada. 🥠
# Create a fortune_cookie.py program that gives the user random fortunes.
# Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:
# Don't pursue happiness – create it.
# All things are difficult before they are easy.
# The early bird gets the worm, but the second mouse gets the cheese.
# Someone in your life needs a letter from you.
# Don't just think. Act!
# Your heart will skip a beat.
# The fortune you search for is in another cookie.
# Help! I'm being held prisoner in a Chinese bakery!
# Make sure to use the random module's random.randint() and an if/elif/else.
# Then, call the fortune() function three times and see what you get!
import random

def fortune():
    cookie = random.randint(1, 8)
    if cookie == 1:
        print('Don\'t pursue happiness – create it.')
    elif cookie == 2:
        print('All things are difficult before they are easy.')
    elif cookie == 3:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif cookie == 4:
        print('Someone in your life needs a letter from you.')
    elif cookie == 5:
        print('Don\'t just think. Act!')
    elif cookie == 6:
        print('Your heart will skip a beat.')
    elif cookie == 7:
        print('The fortune you search for is in another cookie.')
    elif cookie == 8:
        print('Help! I\'m being held prisoner in a Chinese bakery!')

fortune()
fortune()
fortune()

# Bonus: If you're daring, rewrite the function without an if/elif/else.
fortunes = ['Don\'t pursue happiness – create it.',
                'All things are difficult before they are easy.',
                'The early bird gets the worm, but the second mouse gets the cheese.',
                'Someone in your life needs a letter from you.',
                'Don\'t just think. Act!',
                'Your heart will skip a beat.',
                'The fortune you search for is in another cookie.',
                'Help! I\'m being held prisoner in a Chinese bakery!']

def Fortune():
    random_fortune = random.randint(0, len(fortunes) - 1)
    print(fortunes[random_fortune])

Fortune()
Fortune()
Fortune()