# matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import scipy

import random
import timeit

def normal_sum():
    data = [random.random() for i in range(10000)]
    return sum(data)

list(timeit.timeit(normal_sum()))

def np_sum():
    data = np.random.random(10000)
    return np.sum(data)

list(timeit.timeit(np_sum()))




