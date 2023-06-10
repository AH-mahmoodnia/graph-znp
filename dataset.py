import math
class Dataset:
    def __init__(self, size, dimensionality):
        self.size = size
        self.dimensionality = dimensionality
        self.vector_size = self.dimensionality * sizeof(float)
        self.data = [] * self.size
        self.string = None


def minkowskiDist(p1_idx, p2_idx, D , p):
    tmp, dist = 0, 0
    for i in range(D):
        tmp = p1_idx - p2_idx
        dist += abs(tmp) ** p
        p1_idx += 1
        p2_idx += 1
    return math.sqrt(dist)
