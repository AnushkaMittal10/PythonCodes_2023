#Code to print a 3*3 array of random numbers and rounding the float values using numpy
import numpy as np
a = np.random.uniform(low=1, high=5, size = (3,3))
a = np.round(a,2)
print(a)


