import numpy as np


def eucDist(P1, P2):
	d = 0.0
	for ind in range(7):
		a = P1[ind]
		b = P2[ind]
		d += np.square(a - b)
	
	return round(np.sqrt(d), 2)


P1 = np.array([12,13,72,2,5,-15,0])
P2 = np.array([19,5,21,-11,-4,10,41])

result = eucDist(P1,P2)
print(result)
