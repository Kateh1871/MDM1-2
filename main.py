#! usr/bin/env python3


class Graph:
    # stores all information about the parcels including coordinates
    # and an adjancency matrix with the distances between points
    # it is assumed to be a complete graph until the algorithm finds the
    # shortest route
    def __init__(self, width=100, height=100, number=10):
        from random import randint

        # generates a list of coordinates that act as parcel locations
        # includes 1 [middle, middle] coords that act as depot location
        self.vertices = ([[int(width/2), int(height/2)]] +
                         [[randint(0, width), randint(0, height)]
                         for x in range(number)])

        # generates weighted well connected graph based on distances
        # between parcels
        self.matrix = self.GraphGen(self.vertices)

    def GraphGen(self, parcels):
        # generates a well connected weighted graph of the distances between
        # all the parcels
        import numpy as np
        from math import sqrt
        graph = np.empty(shape=(len(parcels), len(parcels)))

        # for each parcel calcuates the distant to every other parcel
        # horribly innefficient since it calculates every distance twice
        for i in range(len(parcels)):
            row = []
            for j in range(len(parcels)):
                row.append(sqrt(((parcels[i][0] - parcels[j][0])**2)
                                + ((parcels[i][1] - parcels[j][1])**2)))
            graph[i] = row

        return graph


def Algorithm(parcels):
    # works by iteratively checking which node is the closest to the
    # current, selecting the new node and checking again
    # distances is the matrix row without the already visited nodes
    # matrixRow is the full row to properly index the new node

    # i actually have no idea if this is the shortest route im just hoping
    # if there are 2 nodes equal distance apart the program breaks, just
    # hope there are none next time and run it again

    visited = []
    current = 0
    for x in range(len(parcels.vertices) - 1):
        visited.append(current)
        print(visited)
        distances = [parcels.matrix[current][y]
                     for y in range(0, len(parcels.matrix[current]))
                     if y not in visited]
        matrixRow = list(parcels.matrix[current])
        new = min(distances)
        current = matrixRow.index(new)

    # 0 is appended onto the end to mark going back to the depo
    visited.append(0)
    print(visited)


parcels = Graph()
# print(parcels.vertices)
# print(parcels.matrix)
Algorithm(parcels)
