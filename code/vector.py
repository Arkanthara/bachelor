import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def print_velocity(dim: int = 2):

    # Combine all possibilities
    element = [-1, 0, 1]
    possible = np.array(np.meshgrid(*[element] * dim)).T.reshape(-1, dim)
    if dim > 2:
        possible = np.array([vec for vec in possible if 0 in vec])
    print(possible)
    origin = np.zeros_like(possible)

    fig = plt.figure()
    plt.title(f"D{dim}Q{len(possible)}")
    ax = fig.add_subplot(111, projection=f"{dim}d")
    ax.set_aspect('equal')
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.5,1.5)
    ax.set_zlim(-1.5, 1.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    ax.quiver(*origin.T, *possible.T)
    plt.show()

print_velocity(3)
