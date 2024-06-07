import matplotlib.pyplot as plt
import numpy as np

particle_nb = 100

positions = np.random.rand(particle_nb, 2)
speed = np.random.uniform(0.1, 0.15, size=(particle_nb, 2))

plt.figure()
plt.title("Représentation des populations de particules")
plt.scatter(positions[:, 0], positions[:, 1], color='g', label="Particule")
plt.quiver(positions[:, 0], positions[:, 1], speed[:, 0], speed[:, 1], scale = 5, width=0.003, color = 'g')
plt.xlim(0, 1)
plt.ylim(0, 1)
ax = plt.gca()
ax.set_aspect(1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)
population = plt.Rectangle((0.6, 0.4), 0.2, 0.2, edgecolor='r', facecolor='none', lw=3, label="Population")
ax.add_patch(population)
plt.legend()
plt.show()
