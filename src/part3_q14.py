# What the function does:
# Author:
# Date:

import numpy as np
import matplotlib.pyplot as plt


def angle():
    angles = np.arange(0, 2*np.pi + np.pi, np.pi/3)
    offset_angle = float(input("Enter the offset angle in degree:"))
    angles_offset = angles + np.deg2rad(offset_angle)

    sin = np.sin(angles_offset)
    cos = np.cos(angles_offset)

    for c, s in zip(cos, sin):
        print((round(c, 4), round(s, 4)))

    plt.plot(cos, sin, marker='.', lw=2)
    plt.title("Question 14")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    angle()
