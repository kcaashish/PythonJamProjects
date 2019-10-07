import numpy as np
import matplotlib.pyplot as plt


def geometry(theta1, theta2, l1, l2):
    [x1, y1] = [0, 0]

    [x2, y2] = [x1 + l1 * np.cos(theta1), y1 + l1 * np.sin(theta1)]

    [x3, y3] = [x2 + l2 * np.cos(theta2), y2 + l2 * np.sin(theta2)]

    xPts = [x1, x2, x3]
    yPts = [y1, y2, y3]

    plt.plot(xPts, yPts, color='black', lw='3')
    plt.axis()
    plt.title("Question 15")
    plt.xlabel(r'x-axis')
    plt.ylabel(r'y-axis')
    plt.show()
    end2array = np.array([round(x3, 2), round(y3, 2)])
    return end2array


if __name__ == '__main__':
    print(geometry(np.pi/8, np.pi/4, 4, 2))


