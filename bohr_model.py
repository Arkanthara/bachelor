import matplotlib.pyplot as plt
import numpy as np

def bohr_model(element: str = 'He', number: int = 2):

    layers = ['g', 'r', 'cyan', 'magenta', 'b', 'orange']

    plt.figure()

    plt.title(f"Atom {element}, Z = {number}")

    # Plot the kern
    plt.scatter(0, 0, s = 2000)
    plt.text(0, 0, element, horizontalalignment='center', verticalalignment='center')

    steps = [2**i for i in range(10)]

    nb_nucleus = number
    
    layer = 1

    theta = np.linspace(0, 2 * np.pi, 200)

    radius = 0

    # Plot the layers
    while nb_nucleus != 0:
        
        layer *= 2

        if layer == 2: layer = 1

        radius += 2

        plt.plot(radius * np.cos(theta), radius * np.sin(theta), 'black', linestyle = ':')

        coordinates = []
        
        for i in range(layer):
            # Convert polar coordinates to rectangular coordinates
            for j in range(2):
                x = radius * np.cos(2 * np.pi * i / (layer) + (np.pi / (20 * radius)) * (-1)**j)
                y = radius * np.sin(2 * np.pi * i / (layer) + (np.pi / (20 * radius)) * (-1)**j)
                coordinates.append((x, y))
        
        index = 0
        while nb_nucleus != 0 and index < layer * 2:
            
            plt.plot(coordinates[index][0], coordinates[index][1], color = layers[int(np.log2(layer) - 1)], marker = 'o')
            index += 1
            nb_nucleus -= 1

        if layer == 1: layer = 2

    plt.gca().set_aspect(1)
    plt.axis('off')
    plt.show()


bohr_model('C', 12)

