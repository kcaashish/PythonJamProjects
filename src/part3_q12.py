import numpy as np
import matplotlib.pyplot as plt


def angle():
    angles = np.arange(0, 2*np.pi + np.pi, np.pi/3)
    sin = np.sin(angles)
    cos = np.cos(angles)

    plt.plot(cos, sin, marker='.')
    plt.title("Question 12")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    angle()
