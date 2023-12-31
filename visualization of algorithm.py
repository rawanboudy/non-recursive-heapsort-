import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def heapify(array, start, end, G):
    current = start
    while (current * 2 + 1) < end:
        left_child = current * 2 + 1
        right_child = current * 2 + 2
        if left_child < end and array[current] < array[left_child]:
            current = left_child
        if right_child < end and array[current] < array[right_child]:
            current = right_child
        if current != start:
            swap(array, current, start)
            update_graph(G, array)
            start = current
        else:
            break


def swap(array, i_one, i_two):
    array[i_one], array[i_two] = array[i_two], array[i_one]


def update_graph(G, array, message=""):
    labels = {i: str(array[i]) for i in range(len(array))}
    pos = hierarchy_pos(G, root = 0)
    nx.draw(G, pos = pos, with_labels = True, labels = labels, node_size = 700, node_color = 'skyblue', font_size = 8)

    # Display the message
    plt.text(0.5, -0.1, message, ha = 'center', va = 'center', transform = plt.gca().transAxes, fontsize = 12,
             bbox = dict(facecolor = 'white', edgecolor = 'white', boxstyle = 'round,pad=0.5'))

    plt.pause(2)  # Adjust pause time as needed
    plt.clf()



def non_recursive_heapsort(array):
    n = len(array)
    i = (n // 2) - 1

    # Visualization Setup
    plt.ion()  # Enable interactive mode
    fig = plt.figure(figsize = (8, 8))
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from([(i, (i - 1) // 2) for i in range(1, n)])

    update_graph(G, array, message = "Building the Heap")

    for i in range(n):
        heapify(array, i, n, G)

    plt.pause(2)  # Pause to display the "The tree is now a heap." message

    i = n - 1
    while i > 0:
        swap(array, i, 0)
        heapify(array, 0, i, G)
        i -= 1

    plt.ioff()  # Disable interactive mode after the sorting is done
    plt.title("Final Sorted Array")
    plt.show(block=False)

# Keep the plot window open until manually closed
#plt.show()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos


def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)

    if len(children) != 0:
        dx = width / 2
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width = dx, vert_gap = vert_gap, vert_loc = vert_loc - vert_gap,
                                 xcenter = nextx, pos = pos, parent = root, parsed = parsed)
    return pos


# Initial Array
array = [10, 52, 4, 9, 20, 44, 11, 3, 8, 12]

# Sorting and Visualization
non_recursive_heapsort(array)
print("Sorted Array:", array)
