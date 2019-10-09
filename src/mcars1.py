import numpy as np
from matplotlib import pyplot as plt


def microcar(expectedList, actualList):
    actualDistArray = np.empty((0, 2), float)
    actualHorDispArray = np.empty((0, 2), float)
    actualVertDispArray = np.empty((0, 2), float)

    expectedDistArray = np.empty((0, 2), float)
    expectedHorDispArray = np.empty((0, 2), float)
    expectedVertDispArray = np.empty((0, 2), float)

    for expectedFile, actualFile in zip(expectedList, actualList):
        expectedValuesRead = open(expectedFile, 'r')
        actualValuesRead = open(actualFile, 'r')

        expectedValues = expectedValuesRead.readlines()
        actualValues = actualValuesRead.readlines()

        expectedValuesRead.close()
        actualValuesRead.close()

        totalActualDistance = 0.0
        totalExpectedDistance = 0.0
        totalActualHorDisp = 0.0
        totalExpectedHorDisp = 0.0
        totalActualVertDisp = 0.0
        totalExpectedVertDisp = 0.0

        for expectedValue, actualValue in zip(expectedValues, actualValues):
            expectedvalues = expectedValue.replace("\n", "").split(",")
            actualvalues = actualValue.replace("\n", "").split(",")

            if actualvalues[-1] == "NA":
                # print("N/A Detected. Ignoring this row")
                continue
            else:
                actualAngle = float(actualvalues[0])
                actualTime = float(actualvalues[1])
                actualSpeed = float(actualvalues[2])

                expectedAngle = float(expectedvalues[0])
                expectedTime = float(expectedvalues[1])
                expectedSpeed = float(expectedvalues[2])

            actualDistanceTravelled = round(actualSpeed * actualTime, 10)
            actualHorDisp = round(actualDistanceTravelled * (np.cos(np.deg2rad(actualAngle))), 10)
            actualVertDisp = round(actualDistanceTravelled * (np.sin(np.deg2rad(actualAngle))), 10)

            expectedDistanceTravelled = round(expectedSpeed * expectedTime, 10)
            expectedHorDisp = round(expectedDistanceTravelled * (np.cos(np.deg2rad(expectedAngle))), 10)
            expectedVertDisp = round(expectedDistanceTravelled * (np.sin(np.deg2rad(expectedAngle))), 10)

            totalActualDistance += actualDistanceTravelled
            totalActualHorDisp += actualHorDisp
            totalActualVertDisp += actualVertDisp

            totalExpectedDistance += expectedDistanceTravelled
            totalExpectedHorDisp += expectedHorDisp
            totalExpectedVertDisp += expectedVertDisp

        totalActualDistance = round(totalActualDistance, 2)
        totalActualHorDisp = round(totalActualHorDisp, 2)
        totalActualVertDisp = round(totalActualVertDisp, 2)
        totalExpectedDistance = round(totalExpectedDistance, 2)
        totalExpectedHorDisp = round(totalExpectedHorDisp, 2)
        totalExpectedVertDisp = round(totalExpectedVertDisp, 2)

        actualDistArray = np.append(actualDistArray, totalActualDistance)
        actualHorDispArray = np.append(actualHorDispArray, totalActualHorDisp)
        actualVertDispArray = np.append(actualVertDispArray, totalActualVertDisp)
        expectedDistArray = np.append(expectedDistArray, totalExpectedDistance)
        expectedHorDispArray = np.append(expectedHorDispArray, totalExpectedHorDisp)
        expectedVertDispArray = np.append(expectedVertDispArray, totalExpectedVertDisp)

    return expectedHorDispArray, expectedVertDispArray, actualHorDispArray, actualVertDispArray, expectedDistArray, actualDistArray


def plotmicrocar(expectedList, actualList):
    expHorDisp, expVerDisp, actHorDisp, actVerDisp, expDist, actDist = microcar(expectedList, actualList)

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
    a1, a2, a3, a4, a5, a6 = microcar(["data/expected1.csv", "data/expected2.csv"], ["data/actual1.csv", "data/actual2.csv"])
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    plotmicrocar(["data/expected1.csv", "data/expected2.csv"], ["data/actual1.csv", "data/actual2.csv"])
