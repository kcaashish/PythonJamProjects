import numpy as np


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


if __name__ == '__main__':
    expectedFiles = ["data/expected1.csv", "data/expected2.csv"]
    actalFiles = ["data/actual1.csv", "data/actual2.csv"]

    a1, a2, a3, a4, a5, a6 = microcar(expectedFiles, actalFiles)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)