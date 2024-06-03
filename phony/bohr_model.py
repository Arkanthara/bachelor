import matplotlib.pyplot as plt
import numpy as np

def bohr_model(element: str = 'He', number: int = 2):

    layers = ['g', 'r', 'cyan', 'magenta', 'b', 'orange', 'yellow']
    name = ["K", "L", "M", 'N', 'O', 'P', 'Q']
    sublayer_name = ['s', 'p', 'd', 'f']
    
    plt.figure()
    plt.title(f"Atome {element}, Z = {number}")

    # Plot the kern
    plt.scatter(0, 0, s = 2000)
    plt.text(0, 0, element, horizontalalignment='center', verticalalignment='center')

    nb_nucleus = number
    theta = np.linspace(0, 2 * np.pi, 200)

    order = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']

    nb_per_layer = {'s': 2, 'p': 6, 'd': 10, 'f': 14}
    index = 0
    layer = 1
    last_layer = 0
    maxlayer = 0
    is_saturated = True

    # Plot the layers
    while nb_nucleus != 0:

        layer = int(order[index][0])
        if layer > maxlayer: maxlayer = layer
        nb = nb_per_layer[order[index][1]]
        pad = 0
        if nb == 6:
            pad = 0.4
        if nb == 10:
            pad = 0.8
        if nb == 14:
            pad = 1.2
        radius = 2 * layer + pad

        if nb > nb_nucleus:
            plt.plot(radius * np.cos(theta), radius * np.sin(theta), 'red', linestyle = ':', label="Couche non saturée")
        else:
            plt.plot(radius * np.cos(theta), radius * np.sin(theta), 'black', linestyle = ':')
        
        for i in range(nb):
            x = radius * np.cos(2 * np.pi * i / nb)
            y = radius * np.sin(2 * np.pi * i / nb)
            if nb_nucleus != 0:
                plt.plot(x, y, color = layers[layer - 1], marker = 'o')
                nb_nucleus -= 1
            else:
                is_saturated = False
                last_layer = i
                break
        plt.text(0, radius, "sous-couche " + order[index], bbox=dict(boxstyle='square', facecolor='lightblue', edgecolor='none'), horizontalalignment='center', verticalalignment='center')
        index += 1
    
    for i in range(maxlayer - 1):
        plt.scatter([], [], color=layers[i], label=f"Couche {name[i]}")

    plt.scatter([], [], color=layers[maxlayer - 1], label=f"Couche {name[maxlayer - 1]} (couche de valence)")

    text = "$"
    for i in range(index - 1):
        text += order[i] + "^{" + str(nb_per_layer[order[i][1]]) + "}"
    if is_saturated:
        text += order[index - 1] + "^{" + str(nb_per_layer[order[index - 1][1]]) + "}$"
    else:
        text += order[index - 1] + "^{" + str(last_layer) + "}$"


    plt.text(0, -2 * (maxlayer + 1), text, horizontalalignment='center', verticalalignment='center')
    plt.gca().set_aspect(1)
    plt.axis('off')
    plt.legend(loc=3)
    plt.show()


bohr_model(input("Atome: "), int(input("Z: ")))

"""
def bohr_model_2(elements: list, numbers: list, title: str = "Molécule $H_2O$"):

    layers = ['g', 'r', 'cyan', 'magenta', 'b', 'orange', 'yellow']
    name = ["K", "L", "M", 'N', 'O', 'P', 'Q']
    sublayer_name = ['s', 'p', 'd', 'f']
    
    plt.figure()
    plt.title(title)
    
    decal = 0

    for k in range(len(elements)):

        element = elements[k]
        number = numbers[k]
        # Plot the kern
        plt.scatter(decal, 0, s = 2000)
        plt.text(0, 0, element, horizontalalignment='center', verticalalignment='center')

        nb_nucleus = number
        theta = np.linspace(0, 2 * np.pi, 200)

        order = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']

        nb_per_layer = {'s': 2, 'p': 6, 'd': 10, 'f': 14}
        index = 0
        layer = 1
        last_layer = 0
        maxlayer = 0
        is_saturated = True
        maxradius = 0

        # Plot the layers
        while nb_nucleus != 0:

            layer = int(order[index][0])
            if layer > maxlayer: maxlayer = layer
            nb = nb_per_layer[order[index][1]]
            pad = 0
            if nb == 6:
                pad = 0.4
            if nb == 10:
                pad = 0.8
            if nb == 14:
                pad = 1.2
            radius = 2 * layer + pad
            if radius > maxradius: maxradius = radius

            if nb > nb_nucleus:
                plt.plot(decal + radius * np.cos(theta), radius * np.sin(theta), 'red', linestyle = ':', label="Couche non saturée")
            else:
                plt.plot(decal + radius * np.cos(theta), radius * np.sin(theta), 'black', linestyle = ':')
            
            for i in range(nb):
                x = decal + radius * np.cos(2 * np.pi * i / nb)
                y = radius * np.sin(2 * np.pi * i / nb)
                if nb_nucleus != 0:
                    plt.plot(x, y, color = layers[layer - 1], marker = 'o')
                    nb_nucleus -= 1
                else:
                    is_saturated = False
                    last_layer = i
                    break
            plt.text(decal, radius, "sous-couche " + order[index], bbox=dict(boxstyle='square', facecolor='lightblue', edgecolor='none'), horizontalalignment='center', verticalalignment='center')
            index += 1
        
        for i in range(maxlayer - 1):
            plt.scatter([], [], color=layers[i], label=f"Couche {name[i]}")

        plt.scatter([], [], color=layers[maxlayer - 1], label=f"Couche {name[maxlayer - 1]} (couche de valence)")
        decal = maxradius

    text = "$"
    for i in range(index - 1):
        text += order[i] + "^{" + str(nb_per_layer[order[i][1]]) + "}"
    if is_saturated:
        text += order[index - 1] + "^{" + str(nb_per_layer[order[index - 1][1]]) + "}$"
    else:
        text += order[index - 1] + "^{" + str(last_layer) + "}$"


    plt.text(0, -2 * (maxlayer + 1), text, horizontalalignment='center', verticalalignment='center')
    plt.gca().set_aspect(1)
    plt.axis('off')
    plt.legend(loc=3)
    plt.show()

bohr_model_2(['H', 'O', 'H'], [1, 8, 1])
"""
