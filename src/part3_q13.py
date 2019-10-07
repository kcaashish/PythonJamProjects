import numpy as np
import matplotlib.pyplot as plt


def angle():
    angles = np.arange(0, 2*np.pi + np.pi, np.pi/3)
    angles_offset = angles + np.pi/2
    sin = np.sin(angles_offset)
    cos = np.cos(angles_offset)

    plt.plot(cos, sin, marker='.')
    plt.title("Question 13")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    angle()
