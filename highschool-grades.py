# U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨
# First, ask the user to enter their grade as an integer.
grade = int(input('Enter your grade: '))
# Create a four-year high school grade system using an if/elif/else statement:
# grade is 9, print 'Freshman'
# grade is 10, print 'Sophomore'
# grade is 11, print 'Junior'
# grade is 12, print 'Senior'
# everything else is 'TBD'
if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophmore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')