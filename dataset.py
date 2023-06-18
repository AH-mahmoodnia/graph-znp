import sys


# TODO: why data is not in constructor?
# TODO: strings and string?
class Dataset:
    # constructor <changed!>
    def __init__(self, size, dimensionality):
        self.size = size
        self.dimensionality = dimensionality
        self.data = [[0] * self.dimensionality] * self.size
        self.strings = ""
        self.string = None
        self.elem_min = 0
        self.elem_max = 0

    # get data with index idx
    def get_vector(self, idx):
        return self.data[idx]

    # finding maximum and minimum value of any feature on dataset
    def find_min_max(self):
        elem_min = float("inf")
        elem_max = float("-inf")

        print("Start find the min max")

        for i in range(self.size):
            v = self.get_vector(i)
            for j in range(self.dimensionality):
                if elem_min > v[j]:
                    elem_min = v[j]
                if elem_max < v[j]:
                    elem_max = v[j]

        print("end of find min max")

        self.elem_min = elem_min
        self.elem_max = elem_max

    # set feature value <changed!>
    def set_val(self, data_i, elem_i, val):
        self.data[data_i][elem_i] = val

    # get feature elem_i of data with index data_i
    def get_val(self, data_i, elem_i):
        return self.data[data_i][elem_i]

    # print data with index of idx
    def dump_vector(self, idx):
        v = self.get_vector(idx)
        print(v)

    # p1_idx, p2_idx: points that we measure distance
    # param:
    # D -> dimensionality
    # p -> minkowski parameter
    def minkowskiDist(p1_idx, p2_idx, D, p):
        tmp, dist = 0, 0
        for i in range(D):
            tmp = p1_idx[i] - p2_idx[i]
            dist += abs(tmp) ** p
        return dist ** (1 / p)

    def distance(self, p1, p2):
        ret = 0
        if g_option.distance_type == 0:
            ret = self.minkowskiDist(p1, p2, self.dimensionality, 2)
        elif g_option.distance_type == 1:
            ret = self.minkowskiDist(p1, p2, self.dimensionality, g_option.minkowski_p)
        else:
            sys.exit(1)
        return ret
