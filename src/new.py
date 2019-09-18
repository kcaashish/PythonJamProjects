# it works as volume but get REQUIRED CORRECT ANSWER

import math


def trackFlow(f_in, f_out, r, H, h, t_max, t_open):
    global flow_out
    initialVolume = math.pi * h * r ** 2
    Volumes = list()
    Heights = list()
    Times = list()
    h = 0
    t = 0.0
    Volumes.append(initialVolume)
    Heights.append(h)
    Times.append(t)
    delta_t = 0.1
    n = 0

    # while (t <= t_max) and (h <= H) and (h >= 0):

    if f_in >= f_out:
        while (t <= t_max) and (h <= H) and (h >= 0):
            t += delta_t

            if t > t_open:
                flow_out = f_out
            else:
                flow_out = 0

            v = round(Volumes[n] + (f_in - flow_out) * delta_t, 10)
            if v > 0:
                Volumes.append(v)
            h = round(Heights[n] + (f_in - flow_out) * delta_t / (math.pi * r ** 2), 10)
            if h >= 0:
                Heights.append(h)

            n += 1
            Times.append(t)

        return [round(x, 2) for x in Volumes], [round(x, 2) for x in Heights], [round(x, 2) for x in Times]

    elif f_in < f_out:
        while (t <= t_max) and (h <= H) and (h >= 0):
            if t > t_open:
                flow_out = f_out
            else:
                flow_out = 0

            t += delta_t

            v = round(Volumes[n] + (f_in - flow_out) * delta_t, 10)
            if v > 0:
                Volumes.append(v)
            h = round(Heights[n] + (f_in - flow_out) * delta_t / (math.pi * r ** 2), 10)
            if h >= 0:
                Heights.append(h)

            n += 1
            Times.append(t)
        Times = Times[:-1]

        return [round(x, 2) for x in Volumes], [round(x, 2) for x in Heights], [round(x, 2) for x in Times]

    #     v = round(Volumes[n] + (f_in - flow_out) * delta_t, 10)
    #     if v > 0:
    #         Volumes.append(v)
    #     h = round(Heights[n] + (f_in - flow_out) * delta_t / (math.pi * r ** 2), 10)
    #     if h >= 0:
    #         Heights.append(h)
    #
    #     n += 1
    #     Times.append(t)
    #
    # return [round(x, 2) for x in Volumes], [round(x, 2) for x in Heights], [round(x, 2) for x in Times]


# volumes, heights, times = trackFlow(1, 1, 1, 10, 0, 3, 1)
volumes, heights, times =  trackFlow(1, 5, 1, 10, 0, 5, 2)
# volumes, heights, times = trackFlow(1, 0.5, 1, 10, 0, 3, 1)

print(len(volumes))
print(len(heights))
print(len(times))

print("Volumes ={}".format(volumes))
print("Heights ={}".format(heights))
print("Times ={}".format(times))
