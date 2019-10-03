import sys
import matplotlib.pyplot as plt
import math
import time


inputData = sys.stdin.readlines()
print(inputData)
# str = " "
# for x in msg:
#     str += x
# newls = list(map(int, str.splitlines()))


T = int(inputData[0])
N, M = [int(x) for x in inputData[1].split(" ")]

# numbers = [int(x) for x in sys.stdin.read().split()]
# for num in numbers:
#     print(num)
#
# T = numbers[0]

X = list(map(int, inputData[2].split(" ")))


