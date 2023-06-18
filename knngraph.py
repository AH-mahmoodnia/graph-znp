import numpy as np
import sys

SAMPLED_BRUTEFORCE = 2
RANDOM_SAMPLED_BRUTEFORCE = 3


class kNNItem:
    def __init__(self, id, dist, new_item, visited):
        self.id = id
        self.dist = dist
        self.new_item = new_item
        self.visited = visited


# List of <size> number of nearest neighbors
class kNNList:
    def __init__(self, items, max_dist, size, id, is_exact):
        self.items = items
        self.max_dist = max_dist
        self.size = size
        self.id = id  # id of point that nearest neighbors this represents
        self.is_exact = is_exact


class kNNGraph:
    def __init__(self, size, k, format, list, DS):
        self.size = size
        self.k = k
        self.format = format
        self.list = list
        self.DS = DS


def init_kNNGraph(N, K, maxK):
    kNN = kNNGraph()
    # for each node make a list of K nearest neighbors
    kNN.list = [kNNList] * N
    kNN.size = N
    kNN.k = K

    for idx, list in enumerate(kNN.list):
        list.items = [kNNItem] * maxK
        list.size = 0
        list.max_dist = sys.float_info.max
        list.is_exact = False
        list.id = idx

    return kNN


def init_kNNGraph(N, K):
    return init_kNNGraph(N, K, K)


def debug_graph(knng: kNNGraph):
    print("kNN Graph with k=%d", knng.k)

    for i_row in range(10):
        for j in len(knng.k):
            print(knng.list[i_row].items[j].id)


def updatekNN(kNN: kNNGraph, p1, p2, dist):
    # check
    if p1 == p2 and kNN.format != RANDOM_SAMPLED_BRUTEFORCE:
        print("p1=p2=%u", p1)
        print("Error!")
    if p1 >= kNN.size:
        print("p1=%u>=kNN->size", p1)
        print("Error!")
    
    kl:kNNList = kNN.list[p1]
    ki:kNNItem = kl.items
    
    if kl.max_dist > dist | kl.size < kNN.k:
        for i in range(kl.size):
            if kl.size > 0 and ki.id == p2:
                return 0
            if ki.dist > dist | i == kl.size:
                ki.id = p2
                ki.dist = dist
                ki.new_item = True
            
                if kl.size < kNN.k:
                    kl.size = kl.size + 1
                    kl.max_dist = kl.items[kl.size - 1].dist