# We just got home from a trip to South America, specifically Colombia, Peru, and Brazil.

# There is some leftover cash in:
# Colombian pesos
# Peruvian soles
# Brazilian reais

# Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

# Make sure to google the current exchange rate

# Exchange Rates as of July 6, 2024
# Colombian pesos to USD: 0.00024
# Peruvian soles to USD: 0.26
# Brazilian reais to USD: 0.18

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

usd = pesos * 0.00024 + soles * 0.26 + reais * 0.18
print(usd)