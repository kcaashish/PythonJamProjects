import numpy as np


def numToPercentage(n):
    if n <= 1.0:
        return int((np.floor(n*100)))
    else:
        return 100


print(numToPercentage(0.074))
print(numToPercentage(1.2))
