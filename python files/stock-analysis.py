# In this exercise, we will perform a simplified version of a time series analysis
# The stock that we will be analyzing is the $AMC stock in January 2023.
# Here are the stock prices (in dollars) for each of these weekdays:
stock_prices = [34.68,
                36.09,
                34.94,
                33.97,
                34.68,
                35.82,
                43.41,
                44.29,
                44.65,
                53.56,
                49.85,
                48.71,
                48.71,
                49.94,
                48.53,
                47.03,
                46.59,
                48.62,
                44.21,
                47.21]
# Create a stock_analysis.py program that implements three functions:
# price_at(x) that finds the price on a given day x.
def price_at(x):
    return stock_prices[x-1]

# max_price(a, b) that finds the maximum price from day a to day b.
def max_price(a, b):
    mx = 0
    for i in range(a, b + 1):
        mx = max(mx, price_at(i))
    return mx

# min_price(a, b) that finds the minimum price from day a to day b.
def min_price(a, b):
    mn = price_at(a)
    for i in range(a, b + 1):
        mn = min(mn, price_at(i))
    return mn

# The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).
# Make sure to call each function to test if your functions work correctly!
print(price_at(3))
print(max_price(1, 15))
print(min_price(5, 10))