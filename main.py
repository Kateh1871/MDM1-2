#! usr/bin/env python3

def ParcelGen(width=100, height=100, number=10):
    from random import randint
    parcels = []
    for location in range(number):
        parcels.append([randint(0, width), randint(0, height)])
    
    return(parcels)


def GraphGen(parcels):
    import numpy as np
    from math import sqrt
    graph = np.empty(shape=(len(parcels), len(parcels)))
    
    for i in range(len(parcels)):
        row = []
        for j in range(len(parcels)):
            row.append(sqrt(((parcels[i][0] - parcels[j][0])**2)
                            + ((parcels[i][1] - parcels[j][1])**2)))
        graph[i] = row

    return graph


parcels = ParcelGen()
graph = GraphGen(parcels)
print(graph)
