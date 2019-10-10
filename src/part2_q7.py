import numpy as np


def dotproduct(P1,P2):
	sum = 0
	for a, b in zip(P1,P2):
		sum += (a*b)
	return sum


P1 = np.array([20,13,8,-9,12,-1,0])
P2 = np.array([-4,31,78,110,5,9,100])
result = dotproduct(P1,P2)
print(result)
