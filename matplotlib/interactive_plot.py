import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # Turn on interactive mode

x = []
y = []

fig, ax = plt.subplots()

for i in range(10):
    x.append(i)
    y.append(i**2)
    ax.clear()
    ax.plot(x, y)
    plt.draw()
    plt.pause(0.5)  # Allow GUI to update
    plt.ioff()