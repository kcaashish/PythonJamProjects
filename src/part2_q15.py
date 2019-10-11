import numpy as np


def fact(num):
	"""This function calculates the factorial of a given number."""
	result = 1
	for value in range(1, num + 1):
		result *= value
	return result


def Fsum(x, n):
	if len(x.shape) == 1 and x.shape[-1] == 1:
		sum = 0.0
		factNum = 1
		res = np.empty((0, x.shape[0]), float)
		x = x[0]
		for i in range(n):
			if i % 2 == 0:
				sum -= ((x ** i) / fact(factNum))
				factNum += 2
			else:
				sum += ((x ** i) / fact(factNum))
				factNum += 2
		sum = round(sum, 4)
		res = np.append(res, sum)
		return res
	
	elif len(x.shape) == 1 and x.shape[-1] != 1:
		res = np.empty((0, x.shape[0]), float)
		for val in x:
			sum = 0.0
			factNum = 1
			for i in range(n):
				if i % 2 == 0:
					sum -= ((val ** i) / fact(factNum))
					factNum += 2
				else:
					sum += ((val ** i) / fact(factNum))
					factNum += 2
			
			sum = round(sum, 4)
			res = np.append(res, sum)
		return res
	
	else:
		res = np.empty(x.shape, float)
		rowarr = np.empty((0,x[0].size), float)
		for ind, Row in enumerate(x):
			rowarr = np.empty((0, x[0].size), float)
			for val in Row:
				sum = 0.0
				factNum = 1
				for i in range(n):
					if i % 2 == 0:
						sum -= ((val ** i) / fact(factNum))
						factNum += 2
					else:
						sum += ((val ** i) / fact(factNum))
						factNum += 2
				sum = round(sum, 4)
				rowarr = np.append(rowarr, sum)
			res[ind] = rowarr
		return res


print("Example:")
print(Fsum(np.array([[1,2],[2,0]]),100))
print("Test 1:")
print(Fsum(np.array([[5,0],[7,6]]),20))
print("Test 2:")
print(Fsum(np.array([8,4]),10))
print("Test 3:")
print(Fsum(np.array([3,0]),0))