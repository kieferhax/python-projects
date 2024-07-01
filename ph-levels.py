# Chemistry: a program that checks whether a pH level is basic, acidic, or neutral

# Request user to input a value between 0 & 14
ph = float(input("Enter a value between 0 and 14: "))

# Write an if, elif, else statement that:
# if ph is greater than 7, output "Basic"
# if ph is less than 7, output "Acidic"
# Else, output "Neutral"

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")