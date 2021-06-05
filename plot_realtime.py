#!/usr/bin/env python3

import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x_len = 10
xy_range = [0, 10]

start_time = time.time()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 10))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title('Proximal Sensor X-Position over time')
plt.xlabel('X-position (cm)')
plt.ylabel('Y-position (cm)')


def animate(i, ys):
	data = ser.readline()

	xs.append((time.time() - start_time)*1000)
	ys.append(float(data.decode()))

	ys = ys[-x_len:]

	line.set_ydata(ys)

	return line,

ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval= 50, blit=True)
plt.show()