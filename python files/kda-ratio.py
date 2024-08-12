# In some online multiplayer games, there's a KDA ratio to evaluate a player's in-game performance: KDA = (k + a)/d
# k = kills, d = deaths, a = assists
# Write a kda() function that takes in parameters: k, d, a
def kda(k, d, a):
    return (k+a)/d
# This function should calculate and return the KDA ratio that uses these parameters
KDA = kda(50, 2, 20)
print(KDA)