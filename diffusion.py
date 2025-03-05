import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_walk(N, steps, dh):
    positions = np.zeros(N)
    history = np.zeros((steps, N))
    
    for t in range(steps):
        steps_random = np.random.uniform(-dh, dh, N)
        positions += steps_random
        history[t] = positions
    
    return history

N = 10
steps = 100
dh = 1.0

data = random_walk(N, steps, dh)

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(-20, 20)
ax.set_ylim(0, N+1)
ax.set_xlabel("X coordinate")
ax.set_ylabel("Particle number")
points, = ax.plot([], [], 'ko', markersize=3)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    points.set_data(data[frame], np.arange(N)+1)
    return points,

ani = animation.FuncAnimation(fig, update, frames=steps, init_func=init, interval=50, blit=True)
plt.show()