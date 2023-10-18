#Method1
import numpy as np
enter_list = input("Enter your list as (1,2,x...):").split(",")
map_int = map(int, enter_list)
converted_map= list(map_int)
ar1 = np.array(converted_map, dtype = int)
print("The array is:", ar1)
new_ar = np.array([], dtype = int)
for i in ar1:
    if i not in new_ar:
        new_ar = np.append(new_ar, [i])
print(new_ar)

#Method2
import numpy as np
enter_list = input("Enter your list as (1,2,x...):").split(",")
map_int = map(int, enter_list)
converted_map= list(map_int)
print(np.unique(converted_map))
