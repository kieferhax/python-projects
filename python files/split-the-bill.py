# Suppose you and three of your friends all went out for a meal together. 
# The bill comes due, and all of you decide to split the bill evenly.
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

# Using this bill list, calculate the total amount and then divide it four ways.
total = 0
# Initialize the total with zero and loop through the bill list to add everything up.
for item in bill:
    total = total + item

# With the total, store what each person has to pay in a my_share variable and then print the result to the terminal.
my_share = total / 4
print(my_share)