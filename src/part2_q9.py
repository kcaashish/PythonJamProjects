import numpy as np


def eucDist(P1, P2):
	d = 0.0
	for a, b in zip(P1, P2):
		d += np.square(a - b)
	
	return round(np.sqrt(d), 2)


P1 = np.array([41,2,30,21,7,-11])
P2 = np.array([19,3,0,27,-17,32])
result = eucDist(P1,P2)
print(result)
