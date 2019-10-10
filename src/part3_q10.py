import numpy as np
import random
import matplotlib.pyplot as plt


def monteCarloPi(trials):
    # trials = int(input("Enter the number of trials:"))
    trial_list = list(range(1, trials + 1))
    circle_points = 0
    square_points = 0
    calculated_pies = list()

    for i in range(0, trials):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = (rand_x**2 + rand_y**2)

        if origin_dist < 1:
            circle_points += 1

        square_points += 1

        value_pi = (4 * circle_points) / square_points

        calculated_pies.append(value_pi)

    print(calculated_pies[-1])
    error_in_pis = list()

    for pie in calculated_pies:
        error_in_pi = abs(np.pi - pie)
        error_in_pis.append(error_in_pi)

    plt.plot(trial_list, error_in_pis)
    plt.title("Monte-Carlo pi Approximations")
    plt.xlabel("Number of trials")
    plt.ylabel("Error in pi")
    plt.show()


if __name__ == '__main__':
    monteCarloPi(100000)
