import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv


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

    # print(indices[0])
    # print(ln_counts[0])

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
                    if line_count == lnc:
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


def plotmicrocar(expectedList, actualList):
    expDist, expHorDisp, expVerDisp, actDist, actHorDisp, actVerDisp = microcar(expectedList, actualList)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, 4)

    microcars = [1, 2]
    x_indexes = np.arange(len(microcars))
    width = 0.25

    ax1.bar(x_indexes - width, expDist, width=width, color="b", label="Expected")
    ax1.bar(x_indexes, actDist, width=width, color="k", label="Actual")
    ax1.set_xticks(ticks=x_indexes - width/2)
    ax1.set_xticklabels(labels=microcars)
    ax1.set_xlabel("mCar")
    ax1.set_ylabel("Dist")
    ax1.set_title("Distance")
    ax1.legend()

    microcar1 = list()
    microcar2 = list()

    for mic1, mic2 in zip(expHorDisp, expVerDisp):
        microcar1.append(mic1)
        microcar2.append(mic2)

    ax2.scatter(expHorDisp[0], expVerDisp[0], s=100, c='blue', label='Microcar 1')
    ax2.scatter(expHorDisp[1], expVerDisp[1], s=100, c='orange', label='Microcar 2')
    ax2.set_xticks(np.arange(-50, 400, 50))
    ax2.set_yticks(np.arange(-50, 400, 50))
    ax2.set_title("Expected")
    ax2.set_xlabel("x Displacement")
    ax2.set_ylabel("y Disp (m)")
    ax2.legend()

    ax3.scatter(actHorDisp[0], actVerDisp[0], s=100, c='blue', marker='X', label='Microcar 1')
    ax3.scatter(actHorDisp[1], actVerDisp[1], s=100, c='orange', marker='X', label='Microcar 2')
    ax3.set_xticks(np.arange(-50, 400, 50))
    ax3.set_yticks(np.arange(-50, 400, 50))
    ax3.set_title("Actual")
    ax3.set_xlabel("x Displacement")
    ax3.set_ylabel("y Disp (m)")
    ax3.legend()

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    expDist, expHorDisp, expVerDisp, actDist, actHorDisp, actVerDisp = microcar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv'])
    print(expHorDisp)
    print(expVerDisp)
    print(actHorDisp)
    print(actVerDisp)
    print(expDist)
    print(actDist)
    plotmicrocar(['data/expected1.csv', 'data/expected2.csv'], ['data/actual1.csv', 'data/actual2.csv'])
