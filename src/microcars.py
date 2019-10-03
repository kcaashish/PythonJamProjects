import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv
import math


def microcar(expectedList):
    global d
    global dx
    global dy
    for csvFile in expectedList:
        with open(csvFile, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            d = 0
            dx = 0
            dy = 0

            for row in csv_reader:
                try:
                    A = float(row[0])
                    t = float(row[1])
                    s = float(row[2])
                except ValueError:
                    continue

                distance = round(s * t, 10)
                xDisplacement = round(distance * np.cos(np.deg2rad(A)), 10)
                yDisplacement = round(distance * np.sin(np.deg2rad(A)), 10)

                d = d + distance
                dx = dx + xDisplacement
                dy = dy + yDisplacement

                line_count += 1
        return round(d, 2), round(dx, 2), round(dy, 2)
    return round(d, 2), round(dx, 2), round(dy, 2)


expectedList = ['data/actual1.csv', 'data/expected1.csv']
distance, displacementX, displacementY = microcar(expectedList)

print(distance)
print(displacementX)
print(displacementY)


# def plotmicrocar():