import math
class Stat:
    def __init__(self):
        self.mean_old = 0.0
        self.std_old = 0.0
        self.mean = 0.0
        self.std = 0.0
        self.N = 0

    def get_std(self):
        return math.sqrt((self.std)/(self.N - 1))

    def debug_stat(self):
        print(f"mean: {self.mean}, std: {self.get_std()}")

    def push_stat(self, x):
        self.N += 1
        if self.N == 1:
            self.mean_old = self.mean = x
            self.std_old = 0
        else:
            self.mean = self.mean_old + (x - self.mean_old)/self.N
            self.std = self.std_old + (x - self.mean_old)*(x - self.mean)
            self.mean_old = self.mean
            self.std_old = self.std
