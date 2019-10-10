import numpy as np


def dotproduct(P1,P2):
	sum = 0
	for ind in range(3):
		a = P1[ind]
		b = P2[ind]
		sum += (a*b)
	return sum


P1 = np.array([5,2,-13])
P2 = np.array([12,3,6])
result = dotproduct(P1,P2)
print(result)
