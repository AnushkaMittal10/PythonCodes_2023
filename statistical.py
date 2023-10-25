#Code using numpy to print min,max,mean,median of the numbers 
import numpy as np
number = np.array([1,2,3,4,5])
min_number = np.min(number)
max_number = np.max(number)
mean_number = np.mean(number)
median_number = np.median(number)
standard_deviation = np.around(np.std(number),2)
print("Minimum number in the array is:", min_number)
print("Maximum number in the array is:", max_number)
print("Average of the array is:", mean_number)
print("The middle number in the array is:", median_number)
print("The standard deviation is:", standard_deviation)


