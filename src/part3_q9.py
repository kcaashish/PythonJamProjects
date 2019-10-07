from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def spiral(a, b, h, n):
    x_pts = list()
    y_pts = list()
    z_pts = list()

    for i in range(2 * n * 20):
        t = i * (math.pi / 20)

        r = round((a * b * np.exp(-0.04*t)) / np.sqrt((b * np.cos(t)**2) + (a * np.sin(t)**2)), 10)
        x = r * np.cos(t)
        y = r * np.sin(t)
        z = (h * t) / 2 * np.pi * n

        x_pts.append(round(x, 2))
        y_pts.append(round(y, 2))
        z_pts.append(round(z, 2))

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x_pts, y_pts, z_pts, label='Elliptical Spiral')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    spiral(2, 5, 18, 7)
