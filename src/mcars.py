import numpy as np


def microcar(expectedList, actualList):
    for expectedFile, actualFile in zip(expectedList, actualList):
        expectedValuesRead = open(expectedFile, 'r')
        actualValuesRead = open(actualFile, 'r')

        expectedValues = expectedValuesRead.readlines()
        actualValues = actualValuesRead.readlines()

        expectedValuesRead.close()
        actualValuesRead.close()

        for expectedValue, actualValue in zip(expectedValues, actualValues):
            expectedvalues = expectedValue.replace("\n", "").split(",")
            actualvalues = actualValue.replace("\n", "").split(",")

            if actualvalues[-1] == "NA":
                print("N/A Detected. Ignoring this row")
                continue

            else:
                print("***********START***********")
                print("Expected Values: %s" % (expectedvalues))
                print("Actual Values: %s" % (actualvalues))
                print("############END############")


if __name__ == '__main__':
    expectedFiles = ["data/expected1.csv", "data/expected2.csv"]
    actalFiles = ["data/actual1.csv", "data/actual2.csv"]

    microcar(expectedFiles, actalFiles)