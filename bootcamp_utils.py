# bootcamp_utils: A collection of statistical functions

import numpy as np

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

def draw_bs_reps(data, func, size=1):
    replicates = np.empty(size)
    for i in range(size):
        sample = np.random.choice(data, replace=True, size=len(data))
        replicates[i] = func(sample)
    return replicates
