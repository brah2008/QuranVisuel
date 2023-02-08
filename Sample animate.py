import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((5, 5), 1)
ax.add_artist(circle)

speed = 0.05

def animate(i):
    global circle, speed
    x, y = circle.center
    if x + circle.radius > ax.get_xlim()[1] or x - circle.radius < ax.get_xlim()[0]:
        speed = -speed
    circle.center = x + speed, y
    return circle,

ani = animation.FuncAnimation(fig, animate, frames=60, interval=50)

plt.show()
