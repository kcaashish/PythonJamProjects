import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv
import math


def microcar(expectedList, actualList):
    expectedlist = []
    actuallist = []
    d = 0
    dx = 0
    dy = 0
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
        expectedlist.append([round(d, 2), round(dx, 2), round(dy, 2)])

    for csvFile in actualList:
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
        actuallist.append([round(d, 2), round(dx, 2), round(dy, 2)])


    returnable_list = []
    print(len(expectedlist), len(actuallist))

    dxArray = []
    dyArray = []
    dArray = []

    for dx, dy, d in expectedlist:
        dxArray.append(dx)
        dyArray.append(dy)
        dArray.append(d)

    returnable_list.append(dxArray)
    returnable_list.append(dyArray)
    returnable_list.append(dArray)

    dxArray = []
    dyArray = []
    dArray = []

    for dx, dy, d in actuallist:
        dxArray.append(dx)
        dyArray.append(dy)
        dArray.append(d)
    returnable_list.append(dxArray)
    returnable_list.append(dyArray)
    returnable_list.append(dArray)

    for i in range(len(returnable_list)):
        returnable_list[i] = np.array(returnable_list[i])

    return returnable_list


expDistance, expHorDisplacement, expVerDisplacement, actDistance, actHorDisplacement, actVerDisplacement = microcar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv'] )
print(microcar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv']))
print(expHorDisplacement)
print(expVerDisplacement)
print(actHorDisplacement)
print(actVerDisplacement)
print(expDistance)
print(actDistance)


# for i in getList:
#     distance, displacementX, displacementY = i
#     print(distance)
#     print(displacementX)
#     print(displacementY)


# def plotmicrocar():