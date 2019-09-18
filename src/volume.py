# it gets the CORRECT ANSWER

import math


def trackFlow(f_in, f_out, r, H, h, t_max, t_open):
    initial_volume = math.pi * h * r ** 2
    Volumes = list()
    Heights = list()
    Volumes.append(initial_volume)
    Heights.append(h)
    Times = list()
    t = 0.0
    Times.append(t)
    delta_t = 0.1
    n = 0

    while (t <= t_max) and (h <= H) and (h >= 0):

        t += delta_t

        if t >= t_open:
            flow_out = f_out
        else:
            flow_out = 0

        # t += delta_t

        v = round(Volumes[n] + (f_in - flow_out) * delta_t, 10)
        if v > 0:
            Volumes.append(v)
        h = round(Heights[n] + (f_in - flow_out) * delta_t / ((math.pi) * r ** 2), 10)
        if h >= 0:
            Heights.append(h)

        n += 1
        Times.append(t)

    return [round(x, 2) for x in Volumes], [round(x, 2) for x in Heights], [round(x, 2) for x in Times]


# volumes, heights, times = trackFlow(1, 1, 1, 10, 0, 3, 1)
volumes, heights, times = trackFlow(1, 5, 1, 10, 0, 5, 2)
# volumes, heights, times = trackFlow(1, 0.5, 1, 10, 0, 3, 1)

print(len(volumes))
print(len(heights))
print(len(times))

print("Volumes = {}".format(volumes))
print("Heights = {}".format(heights))
print("Times = {}".format(times))
