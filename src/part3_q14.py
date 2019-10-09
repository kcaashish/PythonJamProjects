'''What the function does: First the function makes
a numpy array of angles from 0 to 2pi with increment of
pi/3. It takes angle input for users in the form of degree,
converts the angle into radian and adds it to each of the angles
in the initial numpy array to give an angles_offset array. Then,
two new arrays are made that hold the sine and cosine values of
angles in angles_offset array. Finally, the sine values are plotted
as function of cosine values, i.e. as plt.plot(cosines, sines).
'''
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
