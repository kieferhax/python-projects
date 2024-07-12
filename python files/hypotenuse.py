# If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

# Pythagorean equation looks like: c = √(a**2) + (b**2)

# Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = (a**2 + b**2) ** .5
print(c)