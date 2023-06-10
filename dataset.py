import math
import sys
class Dataset:
    def __init__(self, size, dimensionality):
        self.size = size
        self.dimensionality = dimensionality
        self.data = [[0]*self.dimensionality] * self.size
        self.strings
        self.string = None

    def get_vector(self, idx):
        return self.data[idx]

    def find_min_max(self):
        elem_min = float("inf")
        elem_max = float("-inf")
        print("Start find the min max")
        for i in range(self.size):
            v = get_vector(i)
            for j in range(self.dimensionality):
                if elem_min > v[j]:
                    elem_min = v[j]
                if elem_max < v[j]:
                    elem_max = v[j]
        print("end of find min max")
        self.elem_min = elem_min
        self.elem_max = elem_max

    def set_val(self, data_i, elem_i, val):
        self.data[data_i].insert(elem_i, val)

    def get_val(self, data_i, elem_i):
        return self.data[data_i][elem_i]

    def dump_vector(self, idx):
        v = get_vector(idx)
        print(v)

    def distance(self, p1, p2):
        ret = 0
        if g_option.distance_type == 0:
            ret = minkowskiDist(p1, p2, self.dimensionality, 2)
        elif g_option.distance_type == 1:
            ret = minkowskiDist(p1, p2, self.dimensionality, g_option.minkowski_p)
        else:
            sys.exit(1)
        return ret



# p1_idx, p2_idx: points that we measure the distance between them
# D: number of features, p: minkowski param 
def minkowskiDist(p1_idx, p2_idx, D , p):
    tmp, dist = 0, 0
    for i in range(D):
        tmp = p1_idx[i] - p2_idx[i]
        dist += abs(tmp) ** p
    return dist ** (1/p)


