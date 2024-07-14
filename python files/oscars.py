# Every year at the Oscars, the Academy Award for Best Picture is awarded to a single film.
# It's usually the last award presented and is considered to be the most prestigious.
# Let's use a Python list to document the recent winners!

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist',
  '2010 - The King\'s Speech']

# Google the Best Picture winners from 2020, 2021, and 2022.
new_winners = ['2022 - Everything Everywhere All At Once',
               '2021 - CODA',
               '2020 - Nomadland']

# Then, add them to the front of the best_pictures list.
best_pictures.reverse()
best_pictures.extend(new_winners)
print(best_pictures)