def populationgrowth(fileName, n, r, h, t):
    f = open(fileName, 'w')
    try:
        assert type(n) == int and n >= 0
    except AssertionError:
        f.write("Invalid input for initial population.\n")

    try:
        assert type(r) == float and r > 0
    except AssertionError:
        f.write("Invalid input for growth rate.\n")

    try:
        assert type(h) == float and h > 0
    except AssertionError:
        f.write("Invalid input for hours to achieve growth rate.\n")

    try:
        assert type(t) == float and t > 0
    except AssertionError:
        f.write("Invalid input for hours for population growth.\n")

    if not AssertionError:
        print("All inputs are valid.")
        f.write("All the inputs are valid.\n")

    population = round(n * (r ** (t / h)), 2)

    print("The final population is: " + str(population) + ".\n")

    f.write("The final population is: " + str(population) + ".\n")
    f.close()

    return population


if __name__ == '__main__':
    populationgrowth('organisms.txt', 100, 1.4, 6.0, 14.0)
