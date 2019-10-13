import numpy as np


def numToPercentage(n):
    return int((np.floor(n*100)))


print(numToPercentage(0.074))
print(numToPercentage(1.2))
