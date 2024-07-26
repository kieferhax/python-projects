# In the last exercise, we created a Restaurant class.
class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = None

# In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:
# 'Bob\'s Burgers'
# 'American Diner'
# 4.7
# False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

# Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.
print(vars(bobs_burgers.))