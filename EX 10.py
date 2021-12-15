import numpy as np


def subtract_smooth(x, y):
    y_new = y - median_filter(x, y, 1.)
    return y_new


def median_filter(x, y, width):
    y_new = np.zeros(y.shape)
    for i in range(len(x)):
        y_new[i] = np.median(y[np.abs(x - x[i]) < width * 0.5])
    return y_new


subtract_smooth(np.array([1, 2, 3, 4]), np.array([4, 5, 6, 8]))

# IndexError: boolean index did not match indexed array along dimension 0; dimension is 4 but corresponding
# boolean dimension is 5

# The reason is because len(a) != len(b). Technically speaking, boolean indexing
# pick up the value when boolean value is True and drop the value when corresponding boolean value is False.
# So it needs to have one to one map from original array to the boolean index array. Thus their lengths must be the same.