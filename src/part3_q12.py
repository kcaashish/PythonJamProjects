import numpy as np
import matplotlib.pyplot as plt


def angle():
    angles = np.arange(0, 2*np.pi + np.pi, np.pi/3)
    sin = np.sin(angles)
    cos = np.cos(angles)
    plt.plot(cos, sin)
    plt.show()


if __name__ == '__main__':
    angle()
