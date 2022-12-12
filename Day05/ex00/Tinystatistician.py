import numpy as np
import math


def mean(x):
    if not isinstance(x, list) or not x:
        return None
    return np.sum(x) / len(x)


def median(x):
    if not isinstance(x, list) or not x:
        return None
    x.sort()
    if len(x) % 2:
        return x[int(len(x)/2)]
    else:
        return x[int(len(x)/2 - 1)]


def quartile_rank(i_inf, x):
    x.sort()
    if i_inf == int(i_inf):
        return x[int(i_inf)]
    elif (i_inf * 10) % 10 == 2:
        return (x[int(i_inf)] * 3 + x[int(i_inf) + 1]) / 4
    elif (i_inf * 10) % 10 == 5:
        return (x[int(i_inf)] + x[int(i_inf) + 1]) / 2
    else:
        return (x[int(i_inf)] * 3 + x[int(i_inf) + 1]) / 4


def quartile(x):
    if not isinstance(x, list) or not x:
        return None
    i_f1 = (len(x) + 3)/4
    i_f3 = int(len(x) * 3 + 1) / 4
    return [quartile_rank(i_f1 - 1, x), quartile_rank(i_f3 - 1, x)]


def var(x):
    if not isinstance(x, list) or not x:
        return None
    m = mean(x)
    x_cpy = list(np.multiply(x, x))
    return np.sum(x_cpy)/len(x) - m * m


def std(x):
    return math.sqrt(var(x))


def percentile(x, p):
    if not isinstance(x, list) or not x:
        return None
    if not isinstance(p, int) or p not in range(0, 100):
        return None
    x.sort()
    k = p / 100 * (len(x) - 1)
    prop = int(k) + 1 - k
    return x[int(k)] * (1 - k) + x[int(k) + 1] * k

