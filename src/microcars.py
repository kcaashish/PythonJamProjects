import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv
import math


def microcar(expectedList, actualList):
    expectedlist = list()
    actuallist = list()
    d = 0
    dx = 0
    dy = 0

    for csvFile in actualList:
        with open(csvFile, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            d = 0
            dx = 0
            dy = 0

            indices = list()
            ln_counts = list()

            for row in csv_reader:
                try:
                    A = float(row[0])
                    t = float(row[1])
                    s = float(row[2])
                except ValueError:
                    ind = actualList.index(csvFile)
                    lnc = line_count
                    indices.append(ind)
                    ln_counts.append(lnc)
                    continue

                distance = round(s * t, 10)
                xDisplacement = round(distance * np.cos(np.deg2rad(A)), 10)
                yDisplacement = round(distance * np.sin(np.deg2rad(A)), 10)

                d = d + distance
                dx = dx + xDisplacement
                dy = dy + yDisplacement

                line_count += 1
            # indices.append(ind)
            # ln_counts.append(lnc)
        actuallist.append([round(d, 2), round(dx, 2), round(dy, 2)])

    print(indices[0])
    print(ln_counts[0])

    for csvFile in expectedList:

        # if expectedList.index(csvFile) == ind:
        #     with open(csvFile, mode='r') as intermediateRead:
        #         midReader = csv.reader(intermediateRead, delimiter=',')
        #         lines = list(midReader)
        #         # print(lines)
        #         # print(lnc)
        #         lines[lnc][2] = 'NA'
        #         # print(lines)
        #
        #     with open(csvFile, mode='w') as writeFile:
        #         writer = csv.writer(writeFile)
        #         writer.writerows(lines)
        #         writeFile.close()

        with open(csvFile, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            d = 0
            dx = 0
            dy = 0

            # if expectedList.index(csvFile) == ind:
            #     for row in csv_reader:
            #         if line_count == lnc:
            #             line_count += 1
            #             continue
            #
            #         A = float(row[0])
            #         t = float(row[1])
            #         s = float(row[2])
            #
            #         distance = round(s * t, 10)
            #         xDisplacement = round(distance * np.cos(np.deg2rad(A)), 10)
            #         yDisplacement = round(distance * np.sin(np.deg2rad(A)), 10)
            #
            #         d = d + distance
            #         dx = dx + xDisplacement
            #         dy = dy + yDisplacement
            #
            #         line_count += 1
            # else:
            #     for row in csv_reader:
            #         A = float(row[0])
            #         t = float(row[1])
            #         s = float(row[2])
            #
            #         distance = round(s * t, 10)
            #         xDisplacement = round(distance * np.cos(np.deg2rad(A)), 10)
            #         yDisplacement = round(distance * np.sin(np.deg2rad(A)), 10)
            #
            #         d = d + distance
            #         dx = dx + xDisplacement
            #         dy = dy + yDisplacement
            #
            #         line_count += 1
            for row in csv_reader:
                if expectedList.index(csvFile) == ind:
                    print(csvFile)
                    if line_count == lnc:
                        print(line_count)
                        line_count += 1
                        continue

                A = float(row[0])
                t = float(row[1])
                s = float(row[2])

                distance = round(s * t, 10)
                xDisplacement = round(distance * np.cos(np.deg2rad(A)), 10)
                yDisplacement = round(distance * np.sin(np.deg2rad(A)), 10)

                d = d + distance
                dx = dx + xDisplacement
                dy = dy + yDisplacement

                line_count += 1
        expectedlist.append([round(d, 2), round(dx, 2), round(dy, 2)])

    returnable_list = list()
    # print(len(expectedlist), len(actuallist))

    dxArray = list()
    dyArray = list()
    dArray = list()

    for dx, dy, d in expectedlist:
        dxArray.append(dx)
        dyArray.append(dy)
        dArray.append(d)

    returnable_list.append(dxArray)
    returnable_list.append(dyArray)
    returnable_list.append(dArray)

    dxArray = list()
    dyArray = list()
    dArray = list()

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


expDist, expHorDisp, expVerDisp, actDist, actHorDisp, actVerDisp = microcar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv'])
print(microcar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv']))
print(expHorDisp)
print(expVerDisp)
print(actHorDisp)
print(actVerDisp)
print(expDist)
print(actDist)


# def plotmicrocar():